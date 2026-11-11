"""Render authored kana figures from pinned fonts into an external folder."""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from font_sources import font_path
from source_data import reading_introductions

ROOT=Path(__file__).resolve().parents[1]
# A reading card's answer shows its kana's own row of the gojūon (さ: さ し す せ そ; や: や ゆ よ; わ: わ を;
# ん alone), each kana in its vowel's slot (a i u e o, left to right), its romaji under it, so the row
# teaches its family, irregular readings (shi, chi, tsu, fu) included. The app sets a picture beside a
# text answer across the answer's column (314 pt on a 402-pt phone), so five slots across fix the
# kana's size; the strip is no taller than the kana and their romaji need, so it stands whole on
# the sheet. 1,050 pixels wide: at least the device's pixels on a 3x phone. The app shows one answer
# picture in light and dark alike, so the row is printed on its own paper, as the question is.
CELL=210
COLUMNS=5
W,H=COLUMNS*CELL,268
KANA_SIZE=140
KANA_Y=104
ROMAJI_SIZE=50
ROMAJI_BASELINE=238
REGION=170
FRAME=4
CHART={'paper':'#FAFAF9','ink':'#1A1814','ghost':'#BDBAB3','accent':'#A96808'}
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
def slot(c):
 """A kana's slot in the row, in pixels: its vowel's fifth of the strip, top to bottom."""
 return (CELL*c['column'],0,CELL,H)
def square(c):
 """The square a kana keeps to; the card's own is outlined in gold."""
 x=CELL*c['column']+(CELL-REGION)//2
 return (x,KANA_Y-REGION//2,REGION,REGION)

def row(target,forms,introduced):
 """The target's row: its kana taught by this card in ink (the target among them), the rest ghosts."""
 members=[c for c in forms if c['row']==target['row']]
 taught=[c for c in members if c['id'] in introduced or c==target]
 return taught,[c for c in members if c not in taught]


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
 """Each kana's coverage in its slot, with its romaji under it, drawn once: the places never change."""
 result={}
 for f in forms:
  x,y,w,h=slot(f);sx,sy,sw,sh=square(f)
  # Drawn with a slot's room round it: the kana keeps to its square and its romaji to the slot,
  # so no slot takes in a neighbor's ink.
  room=CELL;probe=Image.new('L',(w+2*room,h+2*room),0)
  text_center(probe,f['kana'],(sx-x+sw//2+room,KANA_Y+room),KANA_SIZE,255)
  b=probe.getbbox()
  if not (room+sx-x<=b[0] and room+sy<=b[1] and b[2]<=room+sx-x+sw and b[3]<=room+sy+sh):raise ValueError('The kana falls outside its square: '+f['id'])
  # Every romaji on one baseline, centred in its slot.
  ImageDraw.Draw(probe).text((w//2+room,ROMAJI_BASELINE+room),f['reading'],font=font(ROMAJI_SIZE),fill=255,anchor='ms')
  b=probe.getbbox()
  if not (room+8<=b[0] and room+8<=b[1] and b[2]<=room+w-8 and b[3]<=room+h-8):raise ValueError('The romaji falls outside its slot: '+f['id'])
  result[f['id']]=probe.crop((room,room,room+w,room+h))
 return result
def figure(members,coverage,roles):
 """The row with each kana and its romaji in its role (ink, ghost or accent), the accent's square outlined."""
 im=Image.new('P',(W,H),0);im.putpalette(palette(CHART))
 for f in members:
  x,y,_,_=slot(f);im.paste(coverage[f['id']].point(level(roles[f['id']])),(x,y))
  if roles[f['id']]=='accent':
   sx,sy,sw,sh=square(f);ImageDraw.Draw(im).rectangle((sx,sy,sx+sw-1,sy+sh-1),outline=1+ROLES.index('accent')*STEPS+STEPS-1,width=FRAME)
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
   taught,ghosts=row(c,forms,introductions[q['id']])
   assets['visibleKana']=[f['id'] for f in taught]
   assets['ghostKana']=[f['id'] for f in ghosts]
   # The card's row, filling in over the course: what this card has taught in ink, the rest faint,
   # the card's kana and its romaji in gold. It's the answer's picture, shown once answered.
   roles={f['id']:'ink' if f in taught else 'ghost' for f in taught+ghosts}|{c['id']:'accent'}
   assets['answer']=save(figure(taught+ghosts,coverage,roles),output,f'rv-kana-{c["id"]}-answer-row.png');record['files'].append(assets['answer'])
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
