"""Author audio once through Azure AI Speech; normal package builds never contact a speech service.

The key is read from the login Keychain at run time and never printed, logged or written."""
import argparse
import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

from audio_processing import normalize, PROCESSING

VOICE, RATE = 'ja-JP-NanamiNeural', '-20%'
REGION = 'switzerlandnorth'
FORMAT = 'riff-24khz-16bit-mono-pcm'  # lossless, at the processing's own 24 kHz
KEYCHAIN = dict(account='azure-speech', service='rectoverso-azure-speech')
ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT/'source/audio'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def engine(region):
    return f'Azure AI Speech ({region}, REST v1, {FORMAT})'


def keychain_key():
    result = subprocess.run(['security', 'find-generic-password', '-a', KEYCHAIN['account'], '-s', KEYCHAIN['service'], '-w'], capture_output=True, text=True)
    if result.returncode or not result.stdout.strip():
        raise SystemExit('No Azure Speech key in the login Keychain (account %(account)s, service %(service)s)' % KEYCHAIN)
    return result.stdout.strip()


def ssml(text, voice=VOICE, rate=RATE):
    attribute = lambda value: escape(value, {'"': '&quot;'})
    return ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="ja-JP">'
            f'<voice name="{attribute(voice)}"><prosody rate="{attribute(rate)}">{escape(text)}</prosody></voice></speak>')


class Azure:
    """One request at a time, paced for the free tier; backs off on 429 and stops on a repeated 401/403."""

    def __init__(self, region, interval):
        self.url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'
        self.interval, self.last, self.denied = interval, 0.0, 0
        self.key = keychain_key()

    def synthesize(self, text, voice, rate, raw):
        body = ssml(text, voice, rate).encode()
        headers = {'Ocp-Apim-Subscription-Key': self.key, 'Content-Type': 'application/ssml+xml', 'X-Microsoft-OutputFormat': FORMAT, 'User-Agent': 'rectoverso-tts'}
        for attempt in range(8):
            time.sleep(max(0.0, self.last+self.interval-time.monotonic()))
            self.last = time.monotonic()
            try:
                with urllib.request.urlopen(urllib.request.Request(self.url, data=body, headers=headers, method='POST'), timeout=60) as response:
                    audio = response.read()
                self.denied = 0
                if audio[:4] != b'RIFF' or audio[8:12] != b'WAVE':
                    raise SystemExit('Azure returned something other than a WAVE file for '+raw.name)
                raw.write_bytes(audio)
                return
            except urllib.error.HTTPError as error:
                if error.code in (401, 403):
                    self.denied += 1
                    if self.denied > 1:
                        raise SystemExit(f'Azure refused the key twice (HTTP {error.code}); stopping')
                    time.sleep(10)
                elif error.code == 429 or error.code >= 500:
                    wait = error.headers.get('Retry-After')
                    time.sleep(float(wait) if wait and wait.isdigit() else min(120, 10*2**attempt))
                else:
                    raise SystemExit(f'Azure answered HTTP {error.code} for {raw.name}')
            except (urllib.error.URLError, TimeoutError):
                time.sleep(min(120, 10*2**attempt))
        raise SystemExit('Azure kept refusing '+raw.name+'; stopping')

    def close(self):
        self.key = None


def record(request, output, raw, region):
    signal = normalize(raw, output)
    return dict(request, sha256=sha(output), voice=request.get('voice', VOICE), rate=request.get('rate', RATE), engine=engine(region),
                rawSHA256=sha(raw), sourceFile=str(raw), processing=PROCESSING, listeningReview='pending', **signal)


def author(requests, cache, region=REGION, interval=3.5, regenerate=False):
    """Append new requests, refusing changes to frozen ones; with regenerate, synthesize every recorded file again from its own request."""
    if cache.resolve().is_relative_to(ROOT):
        raise ValueError('Provider originals belong outside the source repository')
    cache.mkdir(parents=True, exist_ok=True)
    provenance = json.loads((DESTINATION/'provenance.json').read_text())
    known = {row['file']: row for row in provenance}
    if regenerate:
        requests = [{k: row[k] for k in ('file', 'input', 'reading', 'purpose', 'sourceId', 'voice', 'rate') if k in row} for row in provenance]
    speech = None
    try:
        for request in requests:
            name = request['file']
            output = DESTINATION/name
            if name in known and not regenerate:
                row = known[name]
                if row['input'] != request['input'] or sha(output) != row['sha256']:
                    raise ValueError('Changed input or file for frozen audio: '+name)
                continue
            raw = cache/(Path(name).stem+'.wav')
            if not raw.exists():
                speech = speech or Azure(region, interval)
                speech.synthesize(request['input'], request.get('voice', VOICE), request.get('rate', RATE), raw)
            row = record(request, output, raw, region)
            if name in known:
                provenance[provenance.index(known[name])] = row
            else:
                provenance.append(row)
            known[name] = row
            (DESTINATION/'provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+'\n')
            print(name, request['input'], row['seconds'], flush=True)
    finally:
        if speech:
            speech.close()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--requests', type=Path, help='new requests to author (a JSON list)')
    group.add_argument('--regenerate', action='store_true', help='synthesize every recording in provenance.json again')
    p.add_argument('--cache', type=Path, required=True, help='provider originals, outside the repository')
    p.add_argument('--region', default=REGION, help="the Speech resource's region (default %(default)s)")
    p.add_argument('--interval', type=float, default=3.5, help='seconds between requests (default %(default)s)')
    a = p.parse_args()
    author(json.loads(a.requests.read_text()) if a.requests else [], a.cache, a.region, a.interval, a.regenerate)
