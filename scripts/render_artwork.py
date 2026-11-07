"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
W,H=1000,4050
PALETTES={'light':{'paper':'#FAFAF9','ink':'#1A1814','line':'#DDDCD8','accent':'#A96808'},'dark':{'paper':'#211E18','ink':'#EDE6D8','line':'#49443C','accent':'#FFD25B'}}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
@lru_cache(maxsize=20)
def font(size,hand=False,serif=False):
 f=ImageFont.truetype(str(ROOT/'artwork/fonts'/('Yomogi-Regular.ttf' if hand else ('NotoSerifJP.ttf' if serif else 'NotoSansJP.ttf'))),size)
 if not hand:f.set_variation_by_axes([400])
 return f
def text_center(im,text,xy,size,color,hand=False,serif=False):
 d=ImageDraw.Draw(im);f=font(size,hand,serif);b=d.textbbox((0,0),text,font=f)
 d.text((xy[0]-(b[0]+b[2])/2,xy[1]-(b[1]+b[3])/2),text,font=f,fill=color)
def save(im,out,name):
 p=out/name;im.save(p,optimize=True)
 return {'file':name,'width':im.width,'height':im.height,'sha256':sha(p)}
def geometry(c):
 cx=60+176*(c['column']+.5);cy=38+360*c['row']
 return (int(cx-65),int(cy+185),130,70)

def render(output,only_type=None):
 if output.resolve().is_relative_to(ROOT):raise ValueError('Rendered artwork belongs outside the source checkout')
 output.mkdir(parents=True,exist_ok=True)
 kana=json.loads((ROOT/'source/kana.json').read_text())
 questions=[q for p in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(p.read_text())]
 if only_type:questions=[q for q in questions if q['type']==only_type]
 record={'format':1,'fonts':json.loads((ROOT/'artwork/fonts/provenance.json').read_text()),'figures':{},'files':[]}
 for script in ['hira','kata']:
  forms=[c for c in kana if c['script']==script];base_images={}
  for mode,pal in PALETTES.items():
   base=Image.new('RGB',(W,H),pal['paper']);d=ImageDraw.Draw(base)
   for row in range(10):d.line((68,38+(row+1)*360-2,W-68,38+(row+1)*360-2),fill=pal['line'])
   for c in forms:text_center(base,c['kana'],(60+176*(c['column']+.5),38+360*c['row']+56),91,pal['ink'])
   base_images[mode]=base
  for q in [q for q in questions if q['type']=='reading' and q['target'].startswith(script+'-')]:
   c=next(c for c in forms if c['id']==q['target']);assets={}
   regions=[{'id':f['id'],'ordinal':i+1,'kind':'label','geometry':{'kind':'rect','coordinates':[geometry(f)[0]/W,geometry(f)[1]/H,130/W,70/H]},'answer':f['reading']} for i,f in enumerate(forms)]
   for mode,pal in PALETTES.items():
    clean=base_images[mode].copy();cx=60+176*(c['column']+.5);cy=38+360*c['row']
    text_center(clean,c['kana'],(cx,cy+56),91,pal['accent'])
    ImageDraw.Draw(clean).rounded_rectangle((cx-23,cy+108,cx+23,cy+111),radius=1,fill=pal['accent'])
    source=clean.copy()
    for f in forms:
     x,y,w,h=geometry(f);text_center(source,f['reading'],(x+w/2,y+h/2),30,pal['ink'])
    diff=ImageChops.difference(source,clean);allowed=Image.new('RGB',(W,H));ad=ImageDraw.Draw(allowed)
    for f in forms:
     x,y,w,h=geometry(f);ad.rectangle((x,y,x+w-1,y+h-1),fill='white')
    if ImageChops.subtract(diff,allowed).getbbox():raise ValueError('Kana pixels changed outside pronunciation masks')
    for role,im in [('source',source),('clean',clean)]:
     key=role if mode=='light' else 'dark'+role.capitalize()
     assets[key]=save(im,output,f'rv-kana-{c["id"]}-{mode}-{role}.png');record['files'].append(assets[key])
   standalone=Image.new('RGB',(700,500),PALETTES['light']['paper']);text_center(standalone,c['kana'],(350,245),280,PALETTES['light']['ink'])
   assets['question']=save(standalone,output,f'rv-kana-{c["id"]}-question.png');record['files'].append(assets['question'])
   x,y,w,h=geometry(c)
   assets['occlusion']={'imageName':assets['source']['file'],'box':[[x/W,y/H],[w/W,h/H]],'siblings':[{'rect':{'_0':[[geometry(f)[0]/W,geometry(f)[1]/H],[130/W,70/H]]}} for f in forms if f['id']!=c['id']],'label':c['reading'],'mode':'hideAll','ordinal':next(i+1 for i,f in enumerate(forms) if f['id']==c['id']),'imageSize':[W,H]}
   assets['preparation']={'version':1,**{k:assets[k] for k in ['source','clean','darkSource','darkClean']},'masksSHA256':hashlib.sha256(b'').hexdigest(),'mode':'hideAll','regions':regions,'canvas':{'method':'flat-srgb-v1','light':[250/255,250/255,249/255],'dark':[33/255,30/255,24/255]}}
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
