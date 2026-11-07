"""Compare independent APKG semantics and preserve a genuinely studied card."""
import argparse
import hashlib
import io
import json
import sqlite3
import tempfile
import zipfile
from pathlib import Path

import zstandard
from anki.collection import Collection
from anki.import_export_pb2 import ImportAnkiPackageRequest,ImportAnkiPackageOptions

def load(collection,path):
    collection.import_anki_package(ImportAnkiPackageRequest(package_path=str(path.resolve()),options=ImportAnkiPackageOptions(with_scheduling=True,merge_notetypes=True,update_notes=1,update_notetypes=1)))
    collection.models._clear_cache()

def inspect(package,folder):
    folder.mkdir()
    with zipfile.ZipFile(package) as archive:
        with zstandard.ZstdDecompressor().stream_reader(io.BytesIO(archive.read('collection.anki21b'))) as stream:
            database=folder/'source.sqlite';database.write_bytes(stream.read())
    with sqlite3.connect(database) as db:
        decks=sorted(r[0] for r in db.execute('select distinct did from cards'))
        order=[r[0] for r in db.execute('select n.guid from cards c join notes n on n.id=c.nid order by c.due')]
    collection=Collection(str(folder/'collection.anki2'))
    try:
        load(collection,package)
        notes={n.guid:(n.mid,n.fields,sorted(n.tags)) for n in (collection.get_note(id) for id in collection.find_notes(''))}
        mids={value[0] for value in notes.values()}
        schemas={m['id']:{'fields':[(f['name'],f['id']) for f in m['flds']],'templates':[(t['id'],t['qfmt'],t['afmt']) for t in m['tmpls']],'css':m['css'],'mod':m['mod']} for m in collection.models.all() if m['id'] in mids}
        media={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(collection.media.dir()).iterdir() if p.is_file()}
        return dict(notes=notes,schemas=schemas,sourceDeckIDs=decks,authoredOrder=order,media=media,count=collection.card_count())
    finally:collection.close()

def verify(first,second,output):
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent,prefix='independent-rebuild-') as temp:
        root=Path(temp);before=inspect(first,root/'first');after=inspect(second,root/'second')
        if before!=after:
            raise ValueError('Independent build drift: '+', '.join(k for k in before if before[k]!=after[k]))
        collection=Collection(str(root/'upgrade.anki2'))
        try:
            load(collection,first);ids=set(collection.find_cards(''));card=collection.get_card(min(ids));collection.decks.select(card.did)
            studied=collection.sched.getCard()
            if studied is None:raise ValueError('No new card available for real scheduler study')
            collection.sched.answerCard(studied,3)
            def state(c):return(c.id,c.nid,c.did,c.type,c.queue,c.ivl,c.due,c.reps)
            expected=state(collection.get_card(studied.id));load(collection,second)
            if state(collection.get_card(studied.id))!=expected or set(collection.find_cards(''))!=ids:
                raise ValueError('Independent rebuild changed card identity or study progress')
        finally:collection.close()
    digest=hashlib.sha256(json.dumps(before,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    result=dict(cards=before['count'],sourceContentAndIdentitiesExact=True,authoredOrderExact=True,mediaExact=True,inPlaceCardIDsAndProgressPreserved=True,semanticSHA256=digest,archiveBytesMayDiffer=True)
    output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('first',type=Path);p.add_argument('second',type=Path);p.add_argument('output',type=Path);a=p.parse_args();verify(a.first,a.second,a.output)
