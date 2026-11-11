"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from font_sources import font_path
from source_data import reading_introductions

ROOT=Path(__file__).resolve().parents[1]
# A reading figure is its script's whole gojūon chart, always the same: five columns (a i u e o)
# by eleven rows (–, k, s, t, n, h, m, y, r, w, n), CELL units a cell, MARGIN round it, drawn at
# SCALE pixels a unit, so it stays sharp at its largest on a 3x screen; its regions are fractions of it.
CELL=180
MARGIN=20
COLUMNS,ROWS=5,11
W,H=COLUMNS*CELL+2*MARGIN,ROWS*CELL+2*MARGIN
SCALE=3
KANA_SIZE=118
REGION=150
# Each picture is indexed: paper, then STEPS antialiasing steps from paper to ink, to the ghost and
# to gold, so every flat colour stays exact and the file a third of an RGB one's size.
STEPS=16
ROLES=('ink','ghost','accent')
PALETTES={'light':{'paper':'#FAFAF9','ink':'#1A1814','ghost':'#DDDCD8','accent':'#A96808'},'dark':{'paper':'#211E18','ink':'#EDE6D8','ghost':'#49443C','accent':'#FFD25B'}}

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
 """A kana's center in chart units, in the middle of its cell."""
 return MARGIN+CELL*(c['column']+.5),MARGIN+CELL*(c['row']+.5)
def geometry(c):
 """A kana's region in chart units: the square around it that the app outlines."""
 cx,cy=center(c)
 return (cx-REGION/2,cy-REGION/2,REGION,REGION)

def chart(target,forms,introduced):
 """The whole chart: the kana taught by this card in ink (the target among them), the rest ghosts."""
 taught=[c for c in forms if c['id'] in introduced or c==target]
 return taught,[c for c in forms if c not in taught]

def normalized_box(c):
 x,y,w,h=geometry(c)
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
 """Each kana's coverage in its own square, drawn once: the chart's places never change."""
 result={}
 for f in forms:
  x,y,w,h=geometry(f);fx,fy=center(f)
  # Drawn with a cell's room round its square: every kana's glyph keeps to its own square, so no
  # square takes in a neighbor's ink.
  room=CELL*SCALE;probe=Image.new('L',(w*SCALE+2*room,h*SCALE+2*room),0)
  text_center(probe,f['kana'],((fx-x)*SCALE+room,(fy-y)*SCALE+room),KANA_SIZE*SCALE,255)
  b=probe.getbbox()
  if not (room<=b[0] and room<=b[1] and b[2]<=room+w*SCALE and b[3]<=room+h*SCALE):raise ValueError('The kana falls outside its region: '+f['id'])
  im=probe.crop((room,room,room+w*SCALE,room+h*SCALE))
  result[f['id']]=im
 return result
def figure(forms,coverage,roles,pal):
 """The chart with each kana in its role (ink, ghost or accent), or left out (None)."""
 im=Image.new('P',(W*SCALE,H*SCALE),0);im.putpalette(palette(pal))
 for f in forms:
  if roles.get(f['id']):x,y,_,_=geometry(f);im.paste(coverage[f['id']].point(level(roles[f['id']])),(int(x*SCALE),int(y*SCALE)))
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
   taught,ghosts=chart(c,forms,introductions[q['id']])
   # Lit (the deck kit's card payload, "A prepared figure"): the whole chart shown, the card's
   # kana in gold, its square outlined by the app; its reading is the region's title, the answer.
   region={'id':c['id'],'ordinal':ordinals[c['id']],'kind':'label','geometry':{'kind':'rect','coordinates':sum(normalized_box(c),[])},'answer':c['reading'],'title':c['reading']}
   assets['visibleKana']=[f['id'] for f in taught]
   assets['ghostKana']=[f['id'] for f in ghosts]
   size=(W*SCALE,H*SCALE)
   roles={f['id']:'ink' if f in taught else 'ghost' for f in forms}
   for mode,pal in PALETTES.items():
    # Over the course the chart fills in: what this card has taught in ink, the rest faint. The
    # source adds the card's kana in gold; the clean chart leaves its square empty.
    source=figure(forms,coverage,roles|{c['id']:'accent'},pal);clean=figure(forms,coverage,roles|{c['id']:None},pal)
    for role,im in [('source',source),('clean',clean)]:
     key=role if mode=='light' else 'dark'+role.capitalize()
     assets[key]=save(im,output,f'rv-kana-{c["id"]}-chart-{mode}-{role}.png')
     record['files'].append(assets[key])
   standalone=Image.new('RGB',(700,500),PALETTES['light']['paper']);text_center(standalone,c['kana'],(350,245),280,PALETTES['light']['ink'])
   assets['question']=save(standalone,output,f'rv-kana-{c["id"]}-question.png');record['files'].append(assets['question'])
   assets['occlusion']={'imageName':assets['source']['file'],'box':normalized_box(c),'siblings':[],'label':c['reading'],'mode':'hideAll','ordinal':ordinals[c['id']],'imageSize':list(size)}
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
