"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont
from font_sources import font_path
from source_data import reading_introductions

ROOT=Path(__file__).resolve().parents[1]
# A reading chart is laid out in chart units (1,000 wide, three 360-unit rows) and drawn at
# SCALE pixels a unit, so it stays sharp on a 3x screen; its regions are fractions of it.
W,H=1000,4050
ROW_HEIGHT=360
CROP_HEIGHT=3*ROW_HEIGHT
SCALE=3
KANA_SIZE=91
CELL=150
PALETTES={'light':{'paper':'#FAFAF9','ink':'#1A1814','line':'#DDDCD8','accent':'#A96808'},'dark':{'paper':'#211E18','ink':'#EDE6D8','line':'#49443C','accent':'#FFD25B'}}

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
def center(c,top=0):
 """A kana's center in chart units, in the middle of its row."""
 return 60+176*(c['column']+.5),ROW_HEIGHT*c['row']+ROW_HEIGHT/2-top
def geometry(c,top=0):
 """A kana's region in chart units: the square around it that the app outlines."""
 cx,cy=center(c,top)
 return (cx-CELL/2,cy-CELL/2,CELL,CELL)

def reading_window(target,forms,introduced):
 """Keep the three-row frame; draw only already-introduced forms."""
 start=max(0,min(target['row']-1,max(c['row'] for c in forms)-2))
 return start*ROW_HEIGHT,[c for c in forms if start<=c['row']<start+3 and c['id'] in introduced]

def normalized_box(c,top):
 x,y,w,h=geometry(c,top)
 return [[x/W,y/CROP_HEIGHT],[w/W,h/CROP_HEIGHT]]


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
  for q in [q for q in questions if q['type']=='reading' and q['target'].startswith(script+'-')]:
   c=next(c for c in forms if c['id']==q['target']);assets={}
   top,visible=reading_window(c,forms,introductions[q['id']])
   ordinals={f['id']:i+1 for i,f in enumerate(forms)}
   cx,cy=center(c,top);x,y,w,h=geometry(c,top)
   # Lit (the deck kit's card payload, "A prepared figure"): the whole chart shown, the card's
   # kana in gold, its square outlined by the app; its reading is the region's title, the answer.
   region={'id':c['id'],'ordinal':ordinals[c['id']],'kind':'label','geometry':{'kind':'rect','coordinates':sum(normalized_box(c,top),[])},'answer':c['reading'],'title':c['reading']}
   assets['visibleKana']=[f['id'] for f in visible]
   assets['crop']={'top':top,'height':CROP_HEIGHT,'rows':sorted({f['row'] for f in visible})}
   size=(W*SCALE,CROP_HEIGHT*SCALE)
   for mode,pal in PALETTES.items():
    clean=Image.new('RGB',size,pal['paper']);d=ImageDraw.Draw(clean)
    # A divider separates occupied rows only; blank future rows have no ink.
    for row in range(min(f['row'] for f in visible),max(f['row'] for f in visible)):
     ly=(ROW_HEIGHT*(row+1)-top)*SCALE;d.line((68*SCALE,ly,(W-68)*SCALE,ly),fill=pal['line'],width=SCALE)
    for f in visible:
     if f!=c:fx,fy=center(f,top);text_center(clean,f['kana'],(fx*SCALE,fy*SCALE),KANA_SIZE*SCALE,pal['ink'])
    # The source adds the card's kana in gold; the clean chart leaves its square empty.
    source=clean.copy();text_center(source,c['kana'],(cx*SCALE,cy*SCALE),KANA_SIZE*SCALE,pal['accent'])
    changed=ImageChops.difference(source,clean).getbbox()
    if not changed or not (x*SCALE<=changed[0] and y*SCALE<=changed[1] and changed[2]<=(x+w)*SCALE and changed[3]<=(y+h)*SCALE):
     raise ValueError('The kana falls outside its region: '+c['id'])
    for role,im in [('source',source),('clean',clean)]:
     key=role if mode=='light' else 'dark'+role.capitalize()
     assets[key]=save(im,output,f'rv-kana-{c["id"]}-lit-{mode}-{role}.png')
     record['files'].append(assets[key])
   standalone=Image.new('RGB',(700,500),PALETTES['light']['paper']);text_center(standalone,c['kana'],(350,245),280,PALETTES['light']['ink'])
   assets['question']=save(standalone,output,f'rv-kana-{c["id"]}-question.png');record['files'].append(assets['question'])
   assets['occlusion']={'imageName':assets['source']['file'],'box':normalized_box(c,top),'siblings':[],'label':c['reading'],'mode':'hideAll','ordinal':ordinals[c['id']],'imageSize':list(size)}
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
