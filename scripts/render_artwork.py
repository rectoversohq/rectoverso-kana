"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from font_sources import font_path
from source_data import reading_introductions

ROOT=Path(__file__).resolve().parents[1]
# A reading card, and an alternate-form card, asks one kana alone: the kana in a writing square, its
# ink centred, over the square's dashed cross (#12). The figure is lit (the deck kit's "mode":
# "lit"): the region is the square, which the app outlines in gold and centres in the question's
# window. The app opens a lit region with its shorter side at about 44 points, unless the figure's
# fill scale is larger: max(canvas width / figure width, window height / figure height)
# (`OcclusionFraming.openingScale`). The page is wide, so the window's height sets the scale on a
# phone, and the square is half the page's height: 286 points on a 402-point iPhone, 317 at 430,
# 218 on the closed Duo, whose short window keeps room for the answer. In book pose the canvas's
# width sets it: 317 points. At every one of them the square has at least three pixels a point.
W,H=3072,2048
SIDE=1024
SQUARE=((W-SIDE)//2,(H-SIDE)//2,SIDE,SIDE)
# Each face at the size where あ's ink is 753 pixels wide (73.5 % of the square): about half the
# width of a phone's screen. Every kana drawn keeps MARGIN pixels or more from the square's edge.
FACES={'sans':('NotoSansJP.ttf',946),'textbook':('KleeOne-SemiBold.ttf',1067),'serif':('NotoSerifJP.ttf',982)}
MARGIN=64
# The cross: dashes through the square's middle, in the palette's line colour.
GUIDE_LINE,GUIDE_DASH=4,22
PALETTES={'light':{'paper':'#FAFAF9','ink':'#1A1814','ghost':'#BDBAB3','accent':'#A96808'},'dark':{'paper':'#211E18','ink':'#EDE6D8','ghost':'#49443C','accent':'#FFD25B'}}
# After a reading's answer, its kana's row of the chart on a dark strip (さ: さ し す せ そ; や: や ゆ よ;
# わ: わ を; ん alone, in the middle), each kana over its romaji in its vowel's slot: the kana asked
# in gold, the row's kana taught by then in cream, the others faint. The app shows one picture in
# light and dark; the strip is dark in both, as the app's own dark button on a light sheet.
STRIP={'paper':'#1A1814','ink':'#EDE6D8','ghost':'#756E62','accent':'#FFD25B'}
SLOT,STRIP_PAD,STRIP_KANA,STRIP_ROMAJI=200,28,128,50
STRIP_W,STRIP_H=5*SLOT+2*STRIP_PAD,302
# Each figure is indexed: its flat colours, then STEPS antialiasing steps from paper to each ink, so
# every flat colour stays exact (the page's paper is the app's canvas) and the file small.
STEPS=16
STRIP_ROLES=('ink','ghost','accent')

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
@lru_cache(maxsize=20)
def font(size,name='NotoSansJP.ttf'):
 f=ImageFont.truetype(str(font_path(name)),size)
 if name.startswith('Noto'):f.set_variation_by_axes([400])
 return f
def text_center(im,text,xy,size,color,name='NotoSansJP.ttf'):
 d=ImageDraw.Draw(im);f=font(size,name);b=d.textbbox((0,0),text,font=f)
 d.text((xy[0]-(b[0]+b[2])/2,xy[1]-(b[1]+b[3])/2),text,font=f,fill=color)
def save(im,out,name):
 p=out/name;im.save(p,optimize=True)
 return {'file':name,'width':im.width,'height':im.height,'sha256':sha(p)}
def hexrgb(h):return tuple(int(h[i:i+2],16) for i in (1,3,5))
def steps(paper,end):
 return [tuple(round(a+(b-a)*i/STEPS) for a,b in zip(paper,end)) for i in range(1,STEPS+1)]
def level(offset):
 """Maps a glyph's coverage (0 to 255) to its ink's palette index from `offset`; no coverage is 0, the paper."""
 return [0 if a==0 else offset+max(0,-(-a*STEPS//255)-1) for a in range(256)]
def solid(coverage):return coverage.point(lambda a:255 if a else 0)

def normalized_square():
 x,y,w,h=SQUARE
 return [[x/W,y/H],[w/W,h/H]]

@lru_cache(maxsize=None)
def ink(kana,face):
 """The kana's coverage, cut to its ink: what is centred in the square."""
 name,size=FACES[face];probe=Image.new('L',(3*size,3*size),0)
 ImageDraw.Draw(probe).text((size,size),kana,font=font(size,name),fill=255)
 coverage=probe.crop(probe.getbbox())
 if coverage.width>SIDE-2*MARGIN or coverage.height>SIDE-2*MARGIN:raise ValueError('The kana does not keep to its square: '+kana)
 return coverage
def ink_box(kana,face):
 """Where the kana's ink sits on the page, in pixels: centred in the square."""
 coverage=ink(kana,face)
 return ((W-coverage.width)//2,(H-coverage.height)//2,coverage.width,coverage.height)
def page(kana,face,pal):
 """The page: the square's dashed cross, and the kana's ink centred on it; without a kana, the square alone."""
 paper=hexrgb(pal['paper']);im=Image.new('P',(W,H),0)
 im.putpalette([v for c in [paper,hexrgb(pal['ghost'])]+steps(paper,hexrgb(pal['ink'])) for v in c])
 d=ImageDraw.Draw(im);x,y,_,_=SQUARE
 for t in range(0,SIDE,2*GUIDE_DASH):
  end=min(SIDE,t+GUIDE_DASH)-1
  d.rectangle((W//2-GUIDE_LINE//2,y+t,W//2+GUIDE_LINE//2-1,y+end),fill=1)
  d.rectangle((x+t,H//2-GUIDE_LINE//2,x+end,H//2+GUIDE_LINE//2-1),fill=1)
 if kana:
  coverage=ink(kana,face)
  im.paste(coverage.point(level(2)),ink_box(kana,face)[:2],solid(coverage))
 return im

def row(target,forms,introduced):
 """The target's row: its kana taught by this card (the target among them), then the rest."""
 members=[c for c in forms if c['row']==target['row']]
 taught=[c for c in members if c['id'] in introduced or c==target]
 return taught,[c for c in members if c not in taught]
def strip_slot(c,members):
 """The middle of the kana's slot on the strip, in pixels: its vowel's, or the strip's for a row of one."""
 return STRIP_W//2 if len(members)==1 else STRIP_PAD+SLOT*c['column']+SLOT//2
def strip(target,taught,ghosts):
 """The row after the answer: each kana on the line, over its romaji, in its role's colour."""
 paper=hexrgb(STRIP['paper']);im=Image.new('P',(STRIP_W,STRIP_H),0)
 im.putpalette([v for c in [paper]+[s for role in STRIP_ROLES for s in steps(paper,hexrgb(STRIP[role]))] for v in c])
 members=sorted(taught+ghosts,key=lambda c:c['column'])
 for c in members:
  role='accent' if c==target else ('ink' if c in taught else 'ghost')
  for text,size,baseline in ((c['kana'],STRIP_KANA,STRIP_PAD+136),(c['reading'],STRIP_ROMAJI,STRIP_PAD+222)):
   coverage=Image.new('L',(STRIP_W,STRIP_H),0)
   ImageDraw.Draw(coverage).text((strip_slot(c,members),baseline),text,font=font(size),fill=255,anchor='ms')
   im.paste(coverage.point(level(1+STRIP_ROLES.index(role)*STEPS)),(0,0),solid(coverage))
 return im

def lit(output,record,key,item,kana,face,clean,ordinal=1):
 """A lit figure of one kana in its square: its pages in light and dark, the clean ones shared by
 every figure (the square without a kana), and the picture Anki shows as the question."""
 name=FACES[face][0];assets={}
 for mode,pal in PALETTES.items():
  role='source' if mode=='light' else 'darkSource'
  assets[role]=save(page(kana,face,pal),output,f'rv-kana-{key}-square-{mode}-source.png')
  record['files'].append(assets[role]|{'font':name})
  assets['clean' if mode=='light' else 'darkClean']=clean[mode]
 standalone=Image.new('RGB',(700,500),PALETTES['light']['paper'])
 text_center(standalone,kana,(350,245),280,PALETTES['light']['ink'],name)
 assets['question']=save(standalone,output,f'rv-kana-{key}-question.png');record['files'].append(assets['question']|{'font':name})
 region={'id':item['id'],'ordinal':ordinal,'kind':'label','geometry':{'kind':'rect','coordinates':sum(normalized_square(),[])},'answer':item['reading'],'title':item['reading']}
 assets['occlusion']={'imageName':assets['source']['file'],'box':normalized_square(),'siblings':[],'label':item['reading'],'mode':'hideAll','ordinal':ordinal,'imageSize':[W,H]}
 assets['preparation']={'version':1,**{k:assets[k] for k in ['source','clean','darkSource','darkClean']},'masksSHA256':hashlib.sha256(b'').hexdigest(),'mode':'lit','regions':[region],'canvas':{'method':'flat-srgb-v1','light':[250/255,250/255,249/255],'dark':[33/255,30/255,24/255]}}
 return assets

def render(output,only_type=None):
 if output.resolve().is_relative_to(ROOT):raise ValueError('Rendered artwork belongs outside the source checkout')
 output.mkdir(parents=True,exist_ok=True)
 kana=json.loads((ROOT/'source/kana.json').read_text())
 questions=[q for p in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(p.read_text())]
 introductions=reading_introductions(questions)
 if only_type:questions=[q for q in questions if q['type']==only_type]
 record={'format':1,'fonts':json.loads((ROOT/'artwork/fonts/provenance.json').read_text()),'figures':{},'files':[]}
 clean={}
 if any(q['type'] in ('reading','variant') for q in questions):
  for mode,pal in PALETTES.items():
   clean[mode]=save(page(None,None,pal),output,f'rv-kana-square-{mode}-clean.png');record['files'].append(clean[mode]|{'font':'NotoSansJP.ttf'})
 for script in ['hira','kata']:
  forms=[c for c in kana if c['script']==script]
  ordinals={f['id']:i+1 for i,f in enumerate(forms)}
  for q in [q for q in questions if q['type']=='reading' and q['target'].startswith(script+'-')]:
   c=next(c for c in forms if c['id']==q['target'])
   taught,ghosts=row(c,forms,introductions[q['id']])
   assets=lit(output,record,c['id'],c,c['kana'],'sans',clean,ordinals[c['id']])
   # What the answer's row shows as taught, the card among them: the card requires the others.
   assets['visibleKana']=[f['id'] for f in taught]
   assets['ghostKana']=[f['id'] for f in ghosts]
   assets['row']=save(strip(c,taught,ghosts),output,f'rv-kana-{c["id"]}-rowstrip.png');record['files'].append(assets['row']|{'font':'NotoSansJP.ttf'})
   record['figures'][q['id']]=assets
  print('Rendered',sum(q['type']=='reading' and q['target'].startswith(script+'-') for q in questions),script,'reading figures',flush=True)
 # An alternate form is read in the same square, in its own face: a textbook face close to
 # handwriting, or a serif one.
 for q in [q for q in questions if q['type']=='variant']:
  record['figures'][q['id']]=lit(output,record,q['id'],{'id':q['id'],'reading':q['answer']},q['display'],q['fontStyle'],clean)
 # Rule, word, comparison and checkpoint questions keep their isolated figures.
 for q in [q for q in questions if q['type'] not in ['reading','listening','variant']]:
  target=q.get('display',q.get('answerKana',''))
  for mode,pal in PALETTES.items():
   im=Image.new('RGB',(1000,600),pal['paper'])
   text_center(im,target,(500,275),min(230,650//max(1,len(target))),pal['ink'])
   entry=save(im,output,f'rv-kana-{q["id"]}-{mode}.png');record['files'].append(entry)
   entry['font']='NotoSansJP.ttf'
   record['figures'].setdefault(q['id'],{})[mode]=entry
 (output/'artwork.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 return record

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--type',dest='only_type');a=p.parse_args();render(a.output,a.only_type)
