"""Author the six outlined SVG cover masters into a new external folder.

Normal builds render the tracked masters and do not load fonts or stroke sources.
This optional authoring tool uses the deck's pinned fonts and frozen KanjiVG paths.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
from xml.sax.saxutils import escape

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
import numpy as np

from font_sources import font_path
from source_data import ROOT

PALETTES = {
    'light': dict(paper='#FAFAF9', ink='#1A1814', accent='#ED8525', muted='#666462', mask='#E7E6E2'),
    'dark': dict(paper='#211E18', ink='#EDE6D8', accent='#FFD25B', muted='#9A928A', mask='#322E27'),
}
STROKE_SOURCE = ROOT / 'artwork/sources/kanjivg/a.json'


def num(x):
    return f'{x:.4f}'.rstrip('0').rstrip('.') or '0'


def sample(path):
    tokens = re.findall(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+)', path)
    i, pos, points, command = 0, np.zeros(2), [], None
    while i < len(tokens):
        if tokens[i].isalpha():
            command = tokens[i]; i += 1
        if command in ['M', 'm']:
            q = np.array(list(map(float, tokens[i:i+2]))); i += 2
            pos = q + pos if command == 'm' else q
            points.append(pos.copy())
        elif command in ['C', 'c']:
            q = np.array(list(map(float, tokens[i:i+6]))).reshape(3, 2); i += 6
            if command == 'c': q = q + pos
            a = pos.copy()
            for t in np.linspace(0, 1, 100)[1:]:
                points.append((1-t)**3*a + 3*(1-t)**2*t*q[0] + 3*(1-t)*t*t*q[1] + t**3*q[2])
            pos = q[2]
        else:
            raise ValueError('Unexpected frozen path command: ' + str(command))
    points = np.array(points)
    distances = np.r_[0, np.cumsum(np.linalg.norm(np.diff(points, axis=0), axis=1))]
    at = np.linspace(0, distances[-1], max(100, round(distances[-1]*8)))
    return np.column_stack([np.interp(at, distances, points[:, k]) for k in [0, 1]]), at


def smooth(t):
    t = np.clip(t, 0, 1)
    return t*t*(3-2*t)


def outline(points, radii):
    tangent = np.gradient(points, axis=0)
    tangent /= np.linalg.norm(tangent, axis=1)[:, None]
    normal = np.column_stack([-tangent[:, 1], tangent[:, 0]])
    left, right = points + normal*radii[:, None], points - normal*radii[:, None]
    # Round caps, matching the app's sampled variable-width brush.
    angle = math.atan2(normal[-1, 1], normal[-1, 0])
    end = [points[-1] + radii[-1]*np.array([math.cos(t), math.sin(t)])
           for t in np.linspace(angle, angle-math.pi, 10)]
    angle = math.atan2(-normal[0, 1], -normal[0, 0])
    start = [points[0] + radii[0]*np.array([math.cos(t), math.sin(t)])
             for t in np.linspace(angle, angle-math.pi, 10)]
    vertices = np.vstack([left, end, right[::-1], start])
    return 'M' + 'L'.join(f'{num(x)},{num(y)}' for x, y in vertices) + 'Z'


def rgb(color):
    return np.array([int(color[i:i+2], 16) for i in [1, 3, 5]])


def brush(strokes, cx, cy, side, palette, count=3, share=1, active=False, added=False):
    scale = side/109
    pieces = [f'<g transform="translate({num(cx-55.5*scale)} {num(cy-56*scale)}) scale({num(scale)})">']
    tip = None
    for j, (points, along) in enumerate(strokes[:count]):
        stop = along[-1]*(share if j == count-1 else 1)
        at = np.r_[along[along < stop], stop]
        points = np.column_stack([np.interp(at, along, points[:, k]) for k in [0, 1]])
        u = at/along[-1]
        radii = 3.2*(.62+.38*smooth(u/.14))*(1-.5*smooth((u-.7)/.3))
        fill = palette['accent'] if added and j == count-1 else palette['ink']
        pieces.append(f'<path fill="{fill}" d="{outline(points, radii)}"/>')
        if active and j == count-1:
            for k in range(1, len(points)):
                warmth = max(0, 1-(stop-at[k])/26)
                if not warmth: continue
                color = np.rint(rgb(palette['ink'])*(1-warmth)+rgb(palette['accent'])*warmth).astype(int)
                fill = '#' + ''.join(f'{c:02x}' for c in color)
                a, b = points[k-1], points[k]
                pieces.append(f'<path d="M{num(a[0])},{num(a[1])}L{num(b[0])},{num(b[1])}" stroke="{fill}" stroke-width="{num(radii[k-1]+radii[k])}" stroke-linecap="round"/>')
            tip = points[-1], radii[-1]
    if tip is not None:
        (x, y), radius = tip
        pieces.append(f'<circle cx="{num(x)}" cy="{num(y)}" r="{num(radius)}" fill="{palette["accent"]}" filter="url(#tip-bloom)"/>')
        pieces.append(f'<circle cx="{num(x)}" cy="{num(y)}" r="{num(radius)}" fill="{palette["accent"]}"/>')
    pieces.append('</g>')
    return '\n'.join(pieces)


class Lettering:
    def __init__(self, name, variable=False):
        self.font = TTFont(font_path(name))
        self.glyphs = self.font.getGlyphSet(location={'wght': 400} if variable else None)
        self.mapping = self.font.getBestCmap()

    def glyph(self, character, cx, cy, palette, *, height=None, size=None):
        name = self.mapping[ord(character)]
        bounds = BoundsPen(self.glyphs); self.glyphs[name].draw(bounds)
        x0, y0, x1, y1 = bounds.bounds
        scale = height/(y1-y0) if height is not None else size/self.font['head'].unitsPerEm
        pen = SVGPathPen(self.glyphs); self.glyphs[name].draw(pen)
        transform = f'translate({num(cx-(x0+x1)*scale/2)} {num(cy+(y0+y1)*scale/2)}) scale({num(scale)} {num(-scale)})'
        return f'<path fill="{palette}" transform="{transform}" d="{pen.getCommands()}"/>'


def make_masters(output):
    output = Path(output).resolve()
    if output.is_relative_to(ROOT) or output.exists():
        raise ValueError('Choose a new authoring directory outside the checkout')
    frozen = json.loads(STROKE_SOURCE.read_text())
    assert frozen['character'] == 'あ' and len(frozen['strokes']) == 3
    strokes = [sample(s['path']) for s in frozen['strokes']]
    jp = Lettering('NotoSansJP.ttf', variable=True)
    roman = Lettering('SF-Pro-Text-Regular.otf')
    output.mkdir(parents=True)
    titles = ['The brush, mid-stroke', 'Stroke by stroke', 'Reveal the reading']
    records = []
    for number in [1, 2, 3]:
        for mode, p in PALETTES.items():
            parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="2010" height="1340" viewBox="0 0 2010 1340">',
                     f'<title>{escape(titles[number-1])}</title>',
                     '<desc>Kana gallery cover. The upper-right language-pill corner is clear. Lettering is outlined.</desc>']
            if number == 1:
                parts.append(f'<defs><filter id="tip-bloom" x="-500%" y="-500%" width="1100%" height="1100%" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="4"/></filter></defs>')
            parts.append(f'<rect width="2010" height="1340" fill="{p["paper"]}"/>')
            if number == 1:
                parts.append(brush(strokes, 1005, 650, 830, p, share=.91, active=True))
            elif number == 2:
                for count, x in enumerate([530, 1005, 1480], 1):
                    parts.append(brush(strokes, x, 637, 475, p, count=count, added=True))
                    parts.append(roman.glyph(str(count), x, 1004, p['muted'], size=66))
            else:
                for x, kana in zip([610, 1005, 1400], ['あ', 'い', 'う']):
                    parts.append(jp.glyph(kana, x, 594, p['accent'] if kana == 'い' else p['ink'], height=315))
                    if kana == 'い':
                        parts.append(f'<rect x="{x-133}" y="883" width="266" height="140" rx="34" fill="none" stroke="{p["accent"]}" stroke-width="5"/>')
                        parts.append(roman.glyph('i', x, 952, p['ink'], size=118))
                    else:
                        parts.append(f'<rect x="{x-133}" y="883" width="266" height="140" rx="34" fill="{p["mask"]}"/>')
            parts.append('</svg>')
            file = f'rv-kana-cover-{mode}-{number}.svg'
            target = output/file; target.write_text('\n'.join(parts)+'\n')
            records.append({'file': file, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    return records


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    print(json.dumps(make_masters(parser.parse_args().output), indent=2))
