"""Build one language with Anki's backend; write only outside the source repo."""
import argparse,hashlib,json,shutil,tempfile
from pathlib import Path
from datetime import datetime
from anki.collection import Collection,ExportAnkiPackageOptions
from anki.decks import DeckId
from source_data import ROOT,course,declared
from render_artwork import render
from covers import render_covers

def build(language,out,only_type=None,artwork=None,beginner_trial=False):
 out=out.resolve()
 if out.is_relative_to(ROOT) or out.exists() or out.with_suffix('.rectoverso.json').exists():raise ValueError('Choose a new package outside the source repo')
 out.parent.mkdir(parents=True,exist_ok=True)
 assets_path=artwork or out.parent/'artwork'
 record=json.loads((assets_path/'artwork.json').read_text()) if (assets_path/'artwork.json').exists() else render(assets_path,only_type)
 meta,notes,models,deck=course(language,record,only_type,beginner_trial)
 modified=int(datetime.fromisoformat(meta['contentModifiedAt'].replace('Z','+00:00')).timestamp())
 if out.name!=meta['package']['file']:raise ValueError('Package filename differs from metadata')
 # Gallery covers accompany complete packages, never their Anki media.
 if only_type is None and not beginner_trial:render_covers(out.parent)
 with tempfile.TemporaryDirectory(dir=out.parent,prefix='anki-build-') as temp:
  col=Collection(str(Path(temp)/'collection.anki2'))
  try:
   created={}
   for key,m in models.items():
    nt=col.models.new(m['name'])
    for name in m['fields']:
     f=col.models.new_field(name);f['id']=m['fieldIDs'][name];col.models.add_field(nt,f)
    for template in m['templates']:
     t=col.models.new_template(template['name']);t.update(template);col.models.add_template(nt,t)
    nt.update(id=m['id'],css=m['css'],mod=modified);col.models.update(nt);created[key]=nt
   d=col.decks.new_deck_legacy(False);d.update(id=deck['id'],name=deck['name'],desc=deck['description']);col.decks.update(d)
   for src in notes:
    note=col.new_note(created[src['model']]);note.guid=src['guid'];note.tags=src['tags']
    for key,value in src['fields'].items():note[key]=value
    col.add_note(note,DeckId(deck['id']))
    col.db.execute('update cards set due=? where nid=?',src['due'],note.id)
   for name in meta['pictures']:
    expected=next(f['sha256'] for f in record['files'] if f['file']==name)
    if hashlib.sha256((assets_path/name).read_bytes()).hexdigest()!=expected:raise ValueError('Artwork digest differs: '+name)
    shutil.copyfile(assets_path/name,Path(col.media.dir())/name)
   for name in meta['sounds']:shutil.copyfile(ROOT/'source/audio'/name,Path(col.media.dir())/name)
   if col.card_count()!=len(notes):raise ValueError('Unexpected generated card count')
   col.db.execute('update notes set mod=?',modified)
   col.export_anki_package(out_path=str(out),options=ExportAnkiPackageOptions(with_scheduling=False,with_media=True),limit=None)
  finally:col.close()
 meta['package'].update(bytes=out.stat().st_size,sha256=hashlib.sha256(out.read_bytes()).hexdigest())
 # The complete course's sidecar is the deck kit's: what rectoverso.json declares for the language,
 # plus the package's size and hash. A component or the trial keeps the course's own record.
 sidecar=declared(language)|{'package':meta['package']} if only_type is None and not beginner_trial else meta
 out.with_suffix('.rectoverso.json').write_text(json.dumps(sidecar,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'package':str(out),'cards':len(notes),'component':meta['component'],'language':language}),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--language',choices=['en','fr'],required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--type',dest='only_type');p.add_argument('--beginner-trial',action='store_true');p.add_argument('--artwork',type=Path);a=p.parse_args();build(a.language,a.out,a.only_type,a.artwork,a.beginner_trial)
