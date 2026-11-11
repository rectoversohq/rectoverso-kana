"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from font_sources import font_path
from source_data import reading_introductions

ROOT=Path(__file__).resolve().parents[1]
# A reading card's answer shows its script's whole gojūon chart, always the same: eleven columns
# (–, k, s, t, n, h, m, y, r, w, n), left to right, by five rows (a i u e o), in CELL-pixel cells
# with a MARGIN round them. The app gives a picture beside a text answer a short, wide place (about
# 120 pt high, at most the answer's column wide), so the chart lies on its side, as wide as
# that column on a 3x screen. The app shows one answer picture in light and dark alike, so the
# chart is printed on its own paper.
CELL=92
MARGIN=14
COLUMNS,ROWS=11,5
W,H=COLUMNS*CELL+2*MARGIN,ROWS*CELL+2*MARGIN
KANA_SIZE=61
REGION=78
FRAME=3
CHART={'paper':'#FAFAF9','ink':'#1A1814','ghost':'#CDCBC6','accent':'#A96808'}
PALETTES={'light':{'paper':'#FAFAF9','ink':'#1A1814','accent':'#A96808'},'dark':{'paper':'#211E18','ink':'#EDE6D8','accent':'#FFD25B'}}
# Each chart is indexed: paper, then STEPS antialiasing steps from paper to ink, to the ghost and
# to gold, so every flat colour stays exact and the file small.
STEPS=16
ROLES=('ink','ghost','accent')

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
@lru_cache(maxsize=20)
def font(size,hand=False,serif=False):
 name='Yomogi-Regular.ttf' if hand else ('NotoSerifJP.ttf' if serif else 'NotoSansJP.ttf')
 f=ImageFont.truetype(str(font_path(name)),size)
 if not hand:f.set_variation_by_axes([400])
 return f
def text_center(im,text,xy,size,color,hand=False,serif=False):
 d=ImageDraw.Draw(im);f=font(size,hand,serif);b=d.textbbox((0,0),text,font=f)
 d.text((xy[0]-(b[0]+b[2])/2,xy[1]-(b[1]+b[3])/2),text,font=f,fill=color)
def save(im,out,name):
 p=out/name;im.save(p,optimize=True)
 return {'file':name,'width':im.width,'height':im.height,'sha256':sha(p)}
def center(c):
 """A kana's center in the chart's pixels: its consonant's column, its vowel's row."""
 return MARGIN+CELL*c['row']+CELL//2,MARGIN+CELL*c['column']+CELL//2
def geometry(c):
 """The square a kana keeps to, in pixels; the card's own is outlined in gold."""
 cx,cy=center(c)
 return (cx-REGION//2,cy-REGION//2,REGION,REGION)

def chart(target,forms,introduced):
 """The whole chart: the kana taught by this card in ink (the target among them), the rest ghosts."""
 taught=[c for c in forms if c['id'] in introduced or c==target]
 return taught,[c for c in forms if c not in taught]


def hexrgb(h):return tuple(int(h[i:i+2],16) for i in (1,3,5))
def palette(pal):
 paper=hexrgb(pal['paper']);colors=[paper]
 for role in ROLES:
  end=hexrgb(pal[role]);colors+=[tuple(round(a+(b-a)*i/STEPS) for a,b in zip(paper,end)) for i in range(1,STEPS+1)]
 return [v for c in colors for v in c]
def level(role):
 """Maps a glyph's coverage (0 to 255) to its role's palette index; no coverage is paper."""
 offset=1+ROLES.index(role)*STEPS
 return [0 if a==0 else offset+max(0,-(-a*STEPS//255)-1) for a in range(256)]
def glyphs(forms):
 """Each kana's coverage in its own square, drawn once: the chart's places never change."""
 result={}
 for f in forms:
  x,y,w,h=geometry(f);fx,fy=center(f)
  # Drawn with a cell's room round its square: every kana's glyph keeps to its own square, so no
  # square takes in a neighbor's ink.
  room=CELL;probe=Image.new('L',(w+2*room,h+2*room),0)
  text_center(probe,f['kana'],((fx-x)+room,(fy-y)+room),KANA_SIZE,255)
  b=probe.getbbox()
  if not (room<=b[0] and room<=b[1] and b[2]<=room+w and b[3]<=room+h):raise ValueError('The kana falls outside its region: '+f['id'])
  im=probe.crop((room,room,room+w,room+h))
  result[f['id']]=im
 return result
def figure(forms,coverage,roles):
 """The chart with each kana in its role (ink, ghost or accent), the accent's square outlined."""
 im=Image.new('P',(W,H),0);im.putpalette(palette(CHART))
 for f in forms:
  x,y,_,_=geometry(f);im.paste(coverage[f['id']].point(level(roles[f['id']])),(x,y))
  if roles[f['id']]=='accent':
   x,y,w,h=geometry(f);ImageDraw.Draw(im).rectangle((x,y,x+w-1,y+h-1),outline=1+ROLES.index('accent')*STEPS+STEPS-1,width=FRAME)
 return im

def render(output,only_type=None):
 if output.resolve().is_relative_to(ROOT):raise ValueError('Rendered artwork belongs outside the source checkout')
 output.mkdir(parents=True,exist_ok=True)
 kana=json.loads((ROOT/'source/kana.json').read_text())
 questions=[q for p in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(p.read_text())]
 introductions=reading_introductions(questions)
 if only_type:questions=[q for q in questions if q['type']==only_type]
 record={'format':1,'fonts':json.loads((ROOT/'artwork/fonts/provenance.json').read_text()),'figures':{},'files':[]}
 for script in ['hira','kata']:
  forms=[c for c in kana if c['script']==script]
  coverage=glyphs(forms)
  for q in [q for q in questions if q['type']=='reading' and q['target'].startswith(script+'-')]:
   c=next(c for c in forms if c['id']==q['target']);assets={}
   taught,ghosts=chart(c,forms,introductions[q['id']])
   assets['visibleKana']=[f['id'] for f in taught]
   assets['ghostKana']=[f['id'] for f in ghosts]
   # Over the course the chart fills in: what this card has taught in ink, the rest faint, the
   # card's kana in gold in its outlined square. It's the answer's picture, shown once claimed.
   roles={f['id']:'ink' if f in taught else 'ghost' for f in forms}|{c['id']:'accent'}
   assets['answer']=save(figure(forms,coverage,roles),output,f'rv-kana-{c["id"]}-answer-chart.png');record['files'].append(assets['answer'])
   standalone=Image.new('RGB',(700,500),PALETTES['light']['paper']);text_center(standalone,c['kana'],(350,245),280,PALETTES['light']['ink'])
   assets['question']=save(standalone,output,f'rv-kana-{c["id"]}-question.png');record['files'].append(assets['question'])
   record['figures'][q['id']]=assets
  print('Rendered',sum(q['type']=='reading' and q['target'].startswith(script+'-') for q in questions),script,'reading figures',flush=True)
 # Later question types use isolated word/contrast/alternate figures.
 for q in [q for q in questions if q['type'] not in ['reading','listening']]:
  target=q.get('display',q.get('answerKana',''))
  for mode,pal in PALETTES.items():
   im=Image.new('RGB',(1000,600),pal['paper'])
   text_center(im,target,(500,275),min(230,650//max(1,len(target))),pal['ink'],q.get('handwritten',False),q.get('fontStyle')=='serif')
   entry=save(im,output,f'rv-kana-{q["id"]}-{mode}.png');record['files'].append(entry)
   entry['font']='Yomogi-Regular.ttf' if q.get('handwritten') else ('NotoSerifJP.ttf' if q.get('fontStyle')=='serif' else 'NotoSansJP.ttf')
   record['figures'].setdefault(q['id'],{})[mode]=entry
 (output/'artwork.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 return record

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--type',dest='only_type');a=p.parse_args();render(a.output,a.only_type)
