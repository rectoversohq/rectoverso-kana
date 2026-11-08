"""Validate a rendered component through Anki import/render/study/reimport."""
import argparse,hashlib,html,json,re,tempfile
from pathlib import Path
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
   for cid in ids:
    card=col.get_card(cid);note=col.get_note(card.nid);p=payload(note);seen.add(note.guid)
    front,back=card.question(),card.answer();after=back.split('<hr id="answer">',1)[1]
    assert front.strip() and after.strip() and 'rv-kana-' not in re.sub(r'<[^>]*>','',front)
    direction=next(t.removeprefix('exercise::') for t in note.tags if t.startswith('exercise::'))
    sounds=re.findall(r'\[sound:([^\]]+)\]',note['Front'])
    if direction=='reading':
     assert not sounds and p['kind']=='occlusion' and p['preparation']['mode']=='hideAll'
     assert len(p['preparation']['regions'])==46 and len(p['occlusion']['siblings'])==45
     assert 'Read this kana.' in front or 'Comment se lit ce kana' in front
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
    states.append({'guid':note.guid,'kind':direction,'payloadKind':p['kind'],'note':note['Note'],'front':note['Front'],'instruction':note['Meta'],'answer':note['Back']})
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
