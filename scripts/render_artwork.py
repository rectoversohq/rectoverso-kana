"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from font_sources import font_path
from source_data import reading_introductions

ROOT=Path(__file__).resolve().parents[1]
# A reading card's figure is its kana's own row of the gojūon (さ: さ し す せ そ; や: や ゆ よ; わ: わ を; ん
# alone), each kana in its vowel's slot (a i u e o, left to right), lit (the deck kit's "mode":
# "lit"). The app centres a lit region in the question's window and zooms out until it fits there
# (`OcclusionFraming`), and the window is narrower than the figure's canvas beside the bar or a
# fold: so the region is the row itself, from its first kana to its last, and the whole row stands
# in the window in every pose; the card's kana is the one in gold. The figure is a row's width (half
# a cell either side) and taller than any window is for its width, so the width sets the scale.
# CELL pixels a cell keep it sharp at its largest on a 3x screen.
CELL=340
MARGIN=CELL//2
CELLS_HIGH=14
W,H=5*CELL+2*MARGIN,CELLS_HIGH*CELL
ROW_Y=H//2
KANA_SIZE=224
PALETTES={'light':{'paper':'#FAFAF9','ink':'#1A1814','ghost':'#BDBAB3','accent':'#A96808'},'dark':{'paper':'#211E18','ink':'#EDE6D8','ghost':'#49443C','accent':'#FFD25B'}}
# Each figure is indexed: paper, then STEPS antialiasing steps from paper to ink, to the ghost and
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
def square(c):
 """A kana's cell in the figure, in pixels: its vowel's slot of the row."""
 return (MARGIN+CELL*c['column'],ROW_Y-CELL//2,CELL,CELL)
def span(members):
 """The row's region, in pixels: from its first kana's cell to its last's."""
 first=min(c['column'] for c in members);last=max(c['column'] for c in members)
 return (MARGIN+CELL*first,ROW_Y-CELL//2,CELL*(last-first+1),CELL)

def row(target,forms,introduced):
 """The target's row: its kana taught by this card in ink (the target among them), the rest ghosts."""
 members=[c for c in forms if c['row']==target['row']]
 taught=[c for c in members if c['id'] in introduced or c==target]
 return taught,[c for c in members if c not in taught]

def normalized_box(members):
 x,y,w,h=span(members)
 return [[x/W,y/H],[w/W,h/H]]


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
 """Each kana's coverage in its cell, drawn once: the places never change."""
 result={}
 for f in forms:
  x,y,w,h=square(f)
  # Drawn with a cell's room round it: every kana keeps to its own cell.
  room=CELL;probe=Image.new('L',(w+2*room,h+2*room),0)
  text_center(probe,f['kana'],(w//2+room,h//2+room),KANA_SIZE,255)
  b=probe.getbbox()
  if not (room<=b[0] and room<=b[1] and b[2]<=room+w and b[3]<=room+h):raise ValueError('The kana falls outside its cell: '+f['id'])
  result[f['id']]=probe.crop((room,room,room+w,room+h))
 return result
def figure(members,coverage,roles,pal):
 """The row with each kana in its role (ink, ghost or accent), or left out (None)."""
 im=Image.new('P',(W,H),0);im.putpalette(palette(pal))
 for f in members:
  if roles.get(f['id']):x,y,_,_=square(f);im.paste(coverage[f['id']].point(level(roles[f['id']])),(x,y))
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
  ordinals={f['id']:i+1 for i,f in enumerate(forms)}
  for q in [q for q in questions if q['type']=='reading' and q['target'].startswith(script+'-')]:
   c=next(c for c in forms if c['id']==q['target']);assets={}
   taught,ghosts=row(c,forms,introductions[q['id']])
   members=sorted(taught+ghosts,key=lambda f:f['column'])
   assets['visibleKana']=[f['id'] for f in taught]
   assets['ghostKana']=[f['id'] for f in ghosts]
   # Lit (the deck kit's card payload, "A prepared figure"): the row shown and outlined by the app,
   # the card's kana in gold; its reading is the region's title, the answer.
   region={'id':c['id'],'ordinal':ordinals[c['id']],'kind':'label','geometry':{'kind':'rect','coordinates':sum(normalized_box(members),[])},'answer':c['reading'],'title':c['reading']}
   roles={f['id']:'ink' if f in taught else 'ghost' for f in members}
   size=(W,H)
   for mode,pal in PALETTES.items():
    # Over the course each row fills in. The source adds the card's kana in gold; the clean
    # figure leaves its cell empty.
    source=figure(members,coverage,roles|{c['id']:'accent'},pal);clean=figure(members,coverage,roles|{c['id']:None},pal)
    for role,im in [('source',source),('clean',clean)]:
     key=role if mode=='light' else 'dark'+role.capitalize()
     assets[key]=save(im,output,f'rv-kana-{c["id"]}-litrow-{mode}-{role}.png')
     record['files'].append(assets[key])
   standalone=Image.new('RGB',(700,500),PALETTES['light']['paper']);text_center(standalone,c['kana'],(350,245),280,PALETTES['light']['ink'])
   assets['question']=save(standalone,output,f'rv-kana-{c["id"]}-question.png');record['files'].append(assets['question'])
   assets['occlusion']={'imageName':assets['source']['file'],'box':normalized_box(members),'siblings':[],'label':c['reading'],'mode':'hideAll','ordinal':ordinals[c['id']],'imageSize':list(size)}
   assets['preparation']={'version':1,**{k:assets[k] for k in ['source','clean','darkSource','darkClean']},'masksSHA256':hashlib.sha256(b'').hexdigest(),'mode':'lit','regions':[region],'canvas':{'method':'flat-srgb-v1','light':[250/255,250/255,249/255],'dark':[33/255,30/255,24/255]}}
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
