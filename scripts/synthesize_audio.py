"""Author audio once; normal package builds never contact a speech service."""
import argparse
import asyncio
import hashlib
import json
import subprocess
from pathlib import Path

import edge_tts
import numpy as np

VOICE, RATE = 'ja-JP-NanamiNeural', '-20%'
ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def normalize(raw, output):
    decoded=subprocess.run(['ffmpeg','-v','error','-i',str(raw),'-ac','1','-ar','24000','-f','f32le','pipe:1'],capture_output=True,check=True)
    audio=np.frombuffer(decoded.stdout,dtype='<f4').copy()
    assert len(audio) and np.isfinite(audio).all()
    rms=np.array([np.sqrt(np.mean(audio[i:i+240]**2)) for i in range(0,len(audio),240)])
    active=np.flatnonzero(rms>max(10**(-45/20),float(rms.max())*.025))
    assert len(active),str(raw)
    first,last=int(active[0]*240),min(len(audio),int((active[-1]+1)*240))
    start,end=max(0,first-2400),min(len(audio),last+6000)
    clip=np.concatenate([np.zeros(max(0,2400-(first-start))),audio[start:end],np.zeros(max(0,6000-(end-last)))]).astype('<f4')
    gain=min(10**((-20-20*np.log10(float(np.sqrt(np.mean(audio[first:last]**2)))))/20),10**(10/20),10**(-3/20)/float(np.max(np.abs(clip))))
    clip*=gain
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar','24000','-ac','1','-i','pipe:0','-c:a','libmp3lame','-b:a','64k','-map_metadata','-1',str(output)],input=clip.tobytes(),check=True)
    return dict(seconds=round(len(clip)/24000,4),activitySeconds=round((last-first)/24000,4),gainDB=round(float(20*np.log10(gain)),3))

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
        row=dict(request,sha256=sha(output),voice=VOICE,rate=RATE,engine='edge-tts 7.3.1',rawSHA256=sha(raw),sourceFile=str(raw),processing='100 ms lead; 250 ms tail; constant gain, no time stretch or pitch shift',listeningReview='pending',**signal)
        provenance.append(row);known[name]=row
        (destination/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
        print(name,request['input'],signal['seconds'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--requests',type=Path,required=True);p.add_argument('--cache',type=Path,required=True);a=p.parse_args()
    asyncio.run(author(json.loads(a.requests.read_text()),a.cache))
