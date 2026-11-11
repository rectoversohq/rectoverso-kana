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
     # The question is the big kana alone; the answer is its reading, then its row (#8): each kana
     # over its romaji, what the card has taught in ink, the rest ghosts, the card's own in gold.
     assert not sounds and p['kind']=='basic' and not {'occlusion','preparation','originalOcclusionAnswer'}&set(p)
     target=forms[note.guid.split('-read-',1)[1]]
     script=[c for c in kana if c['script']==target['script']]
     members=[c for c in script if c['row']==target['row']]
     taught=[c for c in members if c['id'] in introduced[question['id']]]
     pictures=re.findall(r'src="([^"]+)"',note['Back'])
     assert pictures==['rv-kana-'+target['id']+'-answer-row.png'] and note['Back'].startswith(target['reading']+'<img ')
     assert re.findall(r'src="([^"]+)"',note['Front'])==['rv-kana-'+target['id']+'-question.png'] and 'answer-row' not in front
     assert pictures[0] not in front and pictures[0] in after
     path=Path(col.media.dir())/pictures[0]
     with Image.open(path) as image:
      assert image.mode=='P' and image.size==(1050,268)
      image=image.convert('RGB')
     paper,ink,ghost,gold=(250,250,249),(26,24,20),(189,186,179),(169,104,8)
     # Each vowel's slot: the kana and its romaji, in one colour; an empty slot is paper.
     for column in range(5):
      found={k for _,k in image.crop((210*column,0,210*column+210,268)).getcolors(1<<24)}
      c=next((m for m in members if m['column']==column),None)
      if c is None:assert found=={paper},(pictures[0],column)
      elif c==target:assert gold in found and ink not in found and ghost not in found,c['id']
      elif c in taught:assert ink in found and ghost not in found and gold not in found,(pictures[0],c['id'])
      else:assert ghost in found and ink not in found and gold not in found,(pictures[0],c['id'])
     assert '[sound:' in note['Back'] and card.answer_av_tags()
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
