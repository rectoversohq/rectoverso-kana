"""Check an existing, studied edition adopts current content and media on update."""
import argparse
import hashlib
import importlib.util
import json
import re
import tempfile
from pathlib import Path
from anki.collection import Collection

spec=importlib.util.spec_from_file_location('rebuild',Path(__file__).with_name('validate-rebuild.py'))
rebuild=importlib.util.module_from_spec(spec);spec.loader.exec_module(rebuild)


def verify(previous,current,output):
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent,prefix='edition-update-') as temporary:
        root=Path(temporary)
        expected=rebuild.inspect(current,root/'expected')
        collection=Collection(str(root/'update.anki2'))
        try:
            rebuild.load(collection,previous)
            ids=set(collection.find_cards(''))
            first=collection.get_card(min(ids));collection.decks.select(first.did)
            studied=collection.sched.getCard();assert studied is not None
            collection.sched.answerCard(studied,3)
            def states():
                return collection.db.all('select id,nid,did,ord,type,queue,due,ivl,factor,reps,lapses,left,odue,odid,flags,data from cards order by id')
            def schema_ids():
                used={collection.get_note(i).mid for i in collection.find_notes('')}
                return {m['id']:([f['id'] for f in m['flds']],[t['id'] for t in m['tmpls']]) for m in collection.models.all() if m['id'] in used}
            before_schemas=schema_ids()
            before=states();before_log=collection.db.all('select * from revlog order by id');note_ids={collection.get_note(n).guid:n for n in collection.find_notes('')}
            rebuild.load(collection,current)
            if states()!=before or collection.db.all('select * from revlog order by id')!=before_log or set(collection.find_cards(''))!=ids:
                raise ValueError('Update changed card identity or study history')
            if schema_ids()!=before_schemas:
                raise ValueError('Update changed model, field or template identity')
            notes={n.guid:n for n in (collection.get_note(i) for i in collection.find_notes(''))}
            if set(notes)!=set(expected['notes']) or {g:n.id for g,n in notes.items()}!=note_ids:
                raise ValueError('Update changed note identity or inventory')
            actual_media=Path(collection.media.dir());renamed={};audio=set()
            def canonical(field,media):
                def sound(match):
                    name=match[1]
                    if isinstance(media,dict):digest=media[name]
                    else:digest=hashlib.sha256((media/name).read_bytes()).hexdigest()
                    audio.add(digest)
                    return '[sound:'+digest+']'
                return re.sub(r'\[sound:([^]]+)\]',sound,field)
            for guid,note in notes.items():
                mid,fields,tags=expected['notes'][guid]
                if note.mid!=mid or sorted(note.tags)!=tags:
                    raise ValueError('Update changed model identity or tags: '+guid)
                for actual,wanted in zip(note.fields,fields,strict=True):
                    if canonical(actual,actual_media)!=canonical(wanted,expected['media']):
                        raise ValueError('Updated note still uses old content or audio: '+guid)
                    old_names=re.findall(r'\[sound:([^]]+)\]',actual)
                    new_names=re.findall(r'\[sound:([^]]+)\]',wanted)
                    for actual_name,source_name in zip(old_names,new_names,strict=True):
                        if actual_name!=source_name:renamed[source_name]=actual_name
            result=dict(cards=len(ids),noteAndCardIDsPreserved=True,modelFieldTemplateIDsPreserved=True,allStudyStatesPreserved=True,reviewLogPreserved=True,
                        updatedContentAndReferencedAudioExact=True,audioDigests=len(audio),ankiRenamedAudio=renamed)
        finally:collection.close()
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='ankiRenamedAudio'}),flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('previous',type=Path);p.add_argument('current',type=Path);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();verify(a.previous,a.current,a.output)
