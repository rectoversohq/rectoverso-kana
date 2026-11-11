"""Validate a rendered component through Anki import/render/study/reimport."""
import argparse,hashlib,html,json,re,tempfile
from pathlib import Path
from PIL import Image, ImageDraw
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from source_data import course,ordered,questions as source_questions

ROOT=Path(__file__).resolve().parents[2]


def verify_kana_detail(card,note,native,question,language):
 expected=' / '.join(question['accepted']) if question['type']=='listening' else question['answerKana']
 assert note['Back']==expected+'[sound:'+question['audio']+']'
 assert note['Romaji']==question['answerReading']
 assert native['resources']==[{'name':'Romaji','text':question['answerReading']}]
 assert card.answer_av_tags()
 back=card.answer().split('<hr id="answer">',1)[1]
 assert '<input type="button"' in back and 'id="rv-details" hidden' in back
 assert '<strong>Romaji</strong>' in back and 'aria-expanded="false"' in back
 assert ('value="Explore"' if language=='en' else 'value="Explorer"') in back
from anki.collection import Collection,ExportAnkiPackageOptions
from anki.import_export_pb2 import ImportAnkiPackageRequest,ImportAnkiPackageOptions

def load(col,path):
 col.import_anki_package(ImportAnkiPackageRequest(package_path=str(path.resolve()),options=ImportAnkiPackageOptions(with_scheduling=True,merge_notetypes=True,update_notes=1,update_notetypes=1)))
 col.models._clear_cache()
def payload(note):
 field=html.unescape(note['RectoVerso']);return json.JSONDecoder().raw_decode(field)[0]
def source_payload(note):
 return json.JSONDecoder().raw_decode(html.unescape(note['fields']['RectoVerso']))[0]
def inspect_export(col,meta,ids):
 """RectoVerso's own export of the deck (the gallery's round trip): the app writes its cards as notes of
 its own note type, each named by its card's id, with no tags. Every source note is there once, by the
 noteID in its payload, with its fields, its kind, what it requires and introduces, its card and book
 ids, and every picture and sound, byte for byte."""
 made,notes,_,_=course(meta['language']);expected={note['guid']:note for note in notes};seen={};states=[]
 for cid in ids:
  card=col.get_card(cid);note=col.get_note(card.nid);p=payload(note);guid=p['noteID']
  assert guid in expected and guid not in seen,guid
  seen[guid]=note;source=expected[guid];native=source_payload(source)
  assert card.question().strip() and card.answer().strip()
  # An occlusion's front is the app's own drawing of it, over the same pictures; another front keeps its
  # words and its pictures (the app wraps a picture in a block); every other field is the source's.
  words=lambda text:re.sub(r'<[^>]*>','',text).strip()
  pictures=lambda text:set(re.findall(r'src=[\"\']([^\"\']+)',text))
  if native['kind']=='occlusion':assert pictures(source['fields']['Front'])<=pictures(note['Front']),(guid,'Front')
  else:assert (words(note['Front']),pictures(note['Front']))==(words(source['fields']['Front']),pictures(source['fields']['Front'])),(guid,'Front')
  for field in ('Back','Kicker','Meta','Example','Note'):assert note[field]==source['fields'][field],(guid,field)
  for key in ('kind','requires','introduces'):assert p.get(key)==native.get(key),(guid,key)
  assert p['card'].lower()==native['card'] and p['book'].lower()==native['book']==made['bookUUID'],guid
  if '[sound:' in note['Front']:assert card.question_av_tags(),guid
  if '[sound:' in note['Back']:assert card.answer_av_tags(),guid
  for media in re.findall(r'(?:src=[\"\']|\[sound:)([^\"\'\]>]+)','\n'.join(note.fields)):
   assert (Path(col.media.dir())/media).is_file(),media
  states.append({'guid':guid,'kind':source_questions_by_id()[source['itemId']]['type'],'payloadKind':p['kind'],'note':note['Note'],'front':note['Front'],'instruction':note['Meta'],'answer':note['Back'],'romaji':''})
 assert set(seen)==set(expected)
 files={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in Path(col.media.dir()).iterdir() if path.is_file()}
 assert set(files)==set(made['pictures'])|set(made['sounds'])
 rendered={f['file']:f['sha256'] for f in json.loads((ROOT/'artwork/artwork.json').read_text())['files']}
 for name in made['pictures']:assert files[name]==rendered[name],name
 for name in made['sounds']:assert files[name]==hashlib.sha256((ROOT/'source/audio'/name).read_bytes()).hexdigest(),name
 return states
def source_questions_by_id():
 return {q['id']:q for q in source_questions()}
def inspect(package,output):
 output.mkdir(parents=True,exist_ok=True);meta=json.loads(package.with_suffix('.rectoverso.json').read_text());count=meta['cards']
 with tempfile.TemporaryDirectory(dir=output,prefix='anki-check-') as tmp:
  col=Collection(str(Path(tmp)/'collection.anki2'))
  try:
   load(col,package);ids=col.find_cards('');assert len(ids)==count
   exported=all(col.get_note(col.get_card(cid).nid).note_type()['name']=='RectoVerso' for cid in ids)
   seen=set();states=inspect_export(col,meta,ids) if exported else []
   kana=json.loads((ROOT/'source/kana.json').read_text());forms={c['id']:c for c in kana}
   introduced={};known=set()
   for q in ordered(source_questions()):
    known.update(q.get('introduces',[]))
    if q['type']=='reading':introduced[q['id']]=known.copy()
   questions={q['id']:q for path in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(path.read_text())}
   for cid in ([] if exported else ids):
    card=col.get_card(cid);note=col.get_note(card.nid);p=payload(note);seen.add(note.guid)
    front,back=card.question(),card.answer();after=back.split('<hr id="answer">',1)[1]
    assert front.strip() and after.strip() and 'rv-kana-' not in re.sub(r'<[^>]*>','',front)
    direction=next(t.removeprefix('exercise::') for t in note.tags if t.startswith('exercise::'))
    sounds=re.findall(r'\[sound:([^\]]+)\]',note['Front'])
    question=questions[note.guid.split('-'+meta['language']+'-',1)[1]]
    assert note['Kicker']==question['instruction'][meta['language']] and note['Kicker'] in front
    if direction in ('listening','contrast'):verify_kana_detail(card,note,p,question,meta['language'])
    else:assert not note['Romaji'] and 'rv-details' not in after and 'resources' not in p
    if direction=='reading':
     # Lit (#8): the whole chart at 3x, no romaji, what the card has taught in ink, the rest ghosts,
     # the card's kana in gold; one region, titled.
     assert not sounds and p['kind']=='occlusion' and p['preparation']['mode']=='lit'
     target=forms[note.guid.split('-read-',1)[1]]
     script=[c for c in kana if c['script']==target['script']]
     taught=[c for c in script if c['id'] in introduced[question['id']]]
     W,H=940,2020
     def square(c):return (20+180*c['column']+15,20+180*c['row']+15,150,150)
     def box(c):x,y,w,h=square(c);return [[x/W,y/H],[w/W,h/H]]
     regions=p['preparation']['regions'];occlusion=p['occlusion']
     assert regions==[{'id':target['id'],'ordinal':script.index(target)+1,'kind':'label','geometry':{'kind':'rect','coordinates':sum(box(target),[])},'answer':target['reading'],'title':target['reading']}]
     assert occlusion['mode']=='hideAll' and occlusion['imageSize']==[3*W,3*H] and occlusion['siblings']==[]
     assert occlusion['ordinal']==script.index(target)+1 and occlusion['box']==box(target)
     assert occlusion['label']==target['reading'] and p['noteID']==note.guid
     assert occlusion['imageName']==p['preparation']['source']['file']
     for role in ['source','clean','darkSource','darkClean']:
      asset=p['preparation'][role];path=Path(col.media.dir())/asset['file']
      assert '-chart-' in asset['file'] and [asset['width'],asset['height']]==[3*W,3*H]
      assert hashlib.sha256(path.read_bytes()).hexdigest()==asset['sha256']
      with Image.open(path) as image:
       image=image.convert('RGB');assert image.size==(3*W,3*H)
       dark=role.startswith('dark');paper=(33,30,24) if dark else (250,250,249);gold=(255,210,91) if dark else (169,104,8)
       ink=(237,230,216) if dark else (26,24,20);ghost=(73,68,60) if dark else (221,220,216)
       blank=tuple((v,v) for v in paper)
       def colors(c):
        x,y,w,h=(3*v for v in square(c));return {k for _,k in image.crop((x,y,x+w,y+h)).getcolors(1<<24)}
       # The source shows the card's kana in gold in its square; the clean chart leaves it empty.
       lit=colors(target)
       assert (gold in lit and ink not in lit) if role in ('source','darkSource') else lit=={paper}
       # Every other kana is drawn: in ink once taught, else a ghost, never both.
       for c in script:
        if c!=target:
         found=colors(c);assert ((ink in found and ghost not in found) if c in taught else (ghost in found and ink not in found)),(asset['file'],c['id'])
       # Nothing else is drawn: no romaji, no headers, no lines.
       rest=image.copy();draw=ImageDraw.Draw(rest)
       for c in script:
        x,y,w,h=(3*v for v in square(c));draw.rectangle((x,y,x+w-1,y+h-1),fill=paper)
       assert rest.getextrema()==blank,('Ink outside the kana',asset['file'])
     assert '[sound:' in note['Back'] and card.answer_av_tags() and p['originalOcclusionAnswer'] in note['Back']
    if direction=='listening':
     assert len(sounds)==1 and note['Front']=='[sound:'+sounds[0]+']' and len(card.question_av_tags())==1 and p['kind']=='basic'
     assert note['Kicker'].strip() and ('Listen' not in note['Meta'] and 'Écoutez' not in note['Meta'])
    if direction=='contrast':
     assert sounds and card.question_av_tags() and card.answer_av_tags() and p['kind']=='basic'
    if direction in ['rule','word','variant','checkpoint']:
     assert not sounds and not card.question_av_tags() and p['kind']=='basic'
     assert '[sound:' in note['Back'] and card.answer_av_tags()
    assert note['Note'].strip()
    for media in re.findall(r'(?:src=[\"\']|\[sound:)([^\"\'\]>]+)', '\n'.join(note.fields)):
     assert (Path(col.media.dir())/media).is_file(),media
    states.append({'guid':note.guid,'kind':direction,'payloadKind':p['kind'],'note':note['Note'],'front':note['Front'],'instruction':note['Meta'],'answer':note['Back'],'romaji':note['Romaji']})
   assert len(states)==count and (exported or len(seen)==count)
   missing=col.media.check().missing;assert not missing,missing
   hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(col.media.dir()).iterdir() if p.is_file()}
   card=col.get_card(ids[0]);col.decks.select(card.did);studied=col.sched.getCard();assert studied is not None
   col.sched.answerCard(studied,3);before=col.get_card(studied.id)
   def state(c):return(c.id,c.nid,c.type,c.queue,c.due,c.reps,c.ivl)
   kept=state(before);load(col,package);assert col.card_count()==count and state(col.get_card(studied.id))==kept
   col.export_anki_package(out_path=str(output/'roundtrip.apkg'),options=ExportAnkiPackageOptions(with_scheduling=True,with_media=True),limit=None)
   report={'cards':count,'language':meta['language'],'component':meta.get('component'),'rectoVersoExport':exported,'import':'pass','frontBack':'pass','media':'pass','realStudy':'pass','reimportPreservesProgress':'pass','audioFiles':len([n for n in hashes if n.endswith('.mp3')]),'imageFiles':len([n for n in hashes if n.endswith('.png')]),'mediaHashes':hashes,'items':states}
   (output/'anki-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
  finally:col.close()
 print(json.dumps({k:v for k,v in report.items() if k not in ['mediaHashes','items']}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('package',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args();inspect(a.package,a.output)
