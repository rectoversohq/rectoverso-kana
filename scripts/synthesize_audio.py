"""Author audio once; normal package builds never contact a speech service."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path

import edge_tts
from audio_processing import normalize, PROCESSING

VOICE, RATE = 'ja-JP-NanamiNeural', '-20%'
ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

async def author(requests,cache):
    if cache.resolve().is_relative_to(ROOT):raise ValueError('Provider originals belong outside the source repository')
    cache.mkdir(parents=True,exist_ok=True)
    destination=ROOT/'source/audio'
    provenance=json.loads((destination/'provenance.json').read_text())
    known={row['file']:row for row in provenance}
    for request in requests:
        name=request['file'];output=destination/name
        if name in known:
            row=known[name]
            if row['input']!=request['input'] or sha(output)!=row['sha256']:raise ValueError('Changed input or file for frozen audio: '+name)
            continue
        raw=cache/name
        if not raw.exists():
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(request['input'],voice=VOICE,rate=RATE).save(str(raw))
                    break
                except Exception:
                    raw.unlink(missing_ok=True)
                    if attempt==2:raise
                    await asyncio.sleep(2)
        signal=normalize(raw,output)
        row=dict(request,sha256=sha(output),voice=VOICE,rate=RATE,engine='edge-tts 7.3.1',rawSHA256=sha(raw),sourceFile=str(raw),processing=PROCESSING,listeningReview='pending',**signal)
        provenance.append(row);known[name]=row
        (destination/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
        print(name,request['input'],signal['seconds'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--requests',type=Path,required=True);p.add_argument('--cache',type=Path,required=True);a=p.parse_args()
    asyncio.run(author(json.loads(a.requests.read_text()),a.cache))
