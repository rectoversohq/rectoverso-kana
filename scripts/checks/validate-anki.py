"""Validate a rendered component through Anki import/render/study/reimport."""
import argparse,hashlib,html,json,re,tempfile
from pathlib import Path
from PIL import Image
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from source_data import ordered,questions as source_questions

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
def inspect(package,output):
 output.mkdir(parents=True,exist_ok=True);meta=json.loads(package.with_suffix('.rectoverso.json').read_text());count=meta['cards']
 with tempfile.TemporaryDirectory(dir=output,prefix='anki-check-') as tmp:
  col=Collection(str(Path(tmp)/'collection.anki2'))
  try:
   load(col,package);ids=col.find_cards('');assert len(ids)==count
   seen=set();states=[]
   kana=json.loads((ROOT/'source/kana.json').read_text());forms={c['id']:c for c in kana}
   introduced={};known=set()
   for q in ordered(source_questions()):
    known.update(q.get('introduces',[]))
    if q['type']=='reading':introduced[q['id']]=known.copy()
   questions={q['id']:q for path in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(path.read_text())}
   for cid in ids:
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
     assert not sounds and p['kind']=='occlusion' and p['preparation']['mode']=='hideAll'
     target=forms[note.guid.split('-read-',1)[1]]
     script=[c for c in kana if c['script']==target['script']]
     start=max(0,min(target['row']-1,8));top=start*360
     visible=[c for c in script if start<=c['row']<start+3 and c['id'] in introduced[question['id']]]
     def box(c):return [[(83+176*c['column'])/1000,(223+360*c['row']-top)/1080],[.13,70/1080]]
     regions=p['preparation']['regions'];occlusion=p['occlusion']
     assert [(r['id'],r['ordinal'],r['answer'],r['geometry']['coordinates']) for r in regions]==[(c['id'],script.index(c)+1,c['reading'],sum(box(c),[])) for c in visible]
     assert occlusion['mode']=='hideAll' and occlusion['imageSize']==[1000,1080]
     assert occlusion['ordinal']==script.index(target)+1 and occlusion['box']==box(target)
     assert occlusion['label']==target['reading'] and p['noteID']==note.guid
     assert occlusion['siblings']==[{'rect':{'_0':box(c)}} for c in visible if c!=target]
     assert occlusion['imageName']==p['preparation']['source']['file']
     for role in ['source','clean','darkSource','darkClean']:
      asset=p['preparation'][role];path=Path(col.media.dir())/asset['file']
      assert '-introduced-' in asset['file'] and [asset['width'],asset['height']]==[1000,1080]
      assert hashlib.sha256(path.read_bytes()).hexdigest()==asset['sha256']
      with Image.open(path) as image:
       assert image.size==(1000,1080)
       dark=role.startswith('dark');paper=(33,30,24) if dark else (250,250,249);gold=(255,210,91) if dark else (169,104,8)
       cx=148+176*target['column'];cy=38+360*target['row']-top
       # The gold glyph remains; a line below it could look like another stroke.
       assert image.crop((cx-23,cy+108,cx+24,cy+112)).getextrema()==tuple((v,v) for v in paper)
       assert gold in image.crop((cx-65,cy-10,cx+65,cy+108)).getdata()
       for future in script:
        if start<=future['row']<start+3 and future not in visible:
         fx=148+176*future['column'];fy=38+360*future['row']-top
         for area in ((fx-65,fy,fx+65,fy+108),(fx-65,fy+185,fx+65,fy+255)):
          assert image.crop(area).getextrema()==tuple((v,v) for v in paper),('Future kana or reading visible',future['id'],question['id'])
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
   assert len(seen)==count
   missing=col.media.check().missing;assert not missing,missing
   hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(col.media.dir()).iterdir() if p.is_file()}
   card=col.get_card(ids[0]);col.decks.select(card.did);studied=col.sched.getCard();assert studied is not None
   col.sched.answerCard(studied,3);before=col.get_card(studied.id)
   def state(c):return(c.id,c.nid,c.type,c.queue,c.due,c.reps,c.ivl)
   kept=state(before);load(col,package);assert col.card_count()==count and state(col.get_card(studied.id))==kept
   col.export_anki_package(out_path=str(output/'roundtrip.apkg'),options=ExportAnkiPackageOptions(with_scheduling=True,with_media=True),limit=None)
   report={'cards':count,'language':meta['language'],'component':meta['component'],'import':'pass','frontBack':'pass','media':'pass','realStudy':'pass','reimportPreservesProgress':'pass','audioFiles':len([n for n in hashes if n.endswith('.mp3')]),'imageFiles':len([n for n in hashes if n.endswith('.png')]),'mediaHashes':hashes,'items':states}
   (output/'anki-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
  finally:col.close()
 print(json.dumps({k:v for k,v in report.items() if k not in ['mediaHashes','items']}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('package',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args();inspect(a.package,a.output)
