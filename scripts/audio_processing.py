"""Offline, constant-gain preparation; no synthesis, pitch or timing changes to speech."""
import subprocess
import numpy as np

SAMPLE_RATE = 24000
WINDOW = 120  # 5 ms; retain low-energy consonants, not just voiced vowels.
LEAD_MS, TAIL_MS = 40, 75
PROCESSING = '40 ms lead; 75 ms tail at -65 dBFS activity; active RMS -20 dBFS, peak <= -3 dBFS; constant gain, no time stretch or pitch shift'


def decode(path):
    result = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-ac', '1', '-ar', str(SAMPLE_RATE), '-f', 'f32le', 'pipe:1'], capture_output=True, check=True)
    return np.frombuffer(result.stdout, dtype='<f4').copy()


def activity(audio):
    if not len(audio) or not np.isfinite(audio).all():
        raise ValueError('Empty or non-finite audio')
    rms = np.array([np.sqrt(np.mean(audio[i:i+WINDOW]**2)) for i in range(0, len(audio), WINDOW)])
    active = np.flatnonzero(rms > 10**(-65/20))
    if not len(active):
        raise ValueError('No audible activity')
    return int(active[0]*WINDOW), min(len(audio), int((active[-1]+1)*WINDOW))


def prepare(audio):
    first, last = activity(audio)
    lead, tail = round(SAMPLE_RATE*LEAD_MS/1000), round(SAMPLE_RATE*TAIL_MS/1000)
    start, end = max(0, first-lead), min(len(audio), last+tail)
    clip = np.pad(audio[start:end], (max(0, lead-first), max(0, last+tail-len(audio)))).astype('<f4')
    # Level by speech-bearing windows; quiet edge material remains in the clip.
    rms = np.array([np.sqrt(np.mean(audio[i:i+WINDOW]**2)) for i in range(first, last, WINDOW)])
    core = rms[rms > max(10**(-45/20), float(rms.max())*.025)]
    level = float(np.sqrt(np.mean(core**2))) if len(core) else float(np.sqrt(np.mean(audio[first:last]**2)))
    gain = min(10**(-20/20)/level, 10**(10/20), 10**(-3/20)/float(np.max(np.abs(clip))))
    clip *= gain
    return clip, dict(seconds=round(len(clip)/SAMPLE_RATE, 4), activitySeconds=round((last-first)/SAMPLE_RATE, 4), gainDB=round(float(20*np.log10(gain)), 3), trimStartSamples=start, trimEndSamples=end)


def normalize(raw, output):
    clip, signal = prepare(decode(raw))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SAMPLE_RATE), '-ac', '1', '-i', 'pipe:0', '-c:a', 'libmp3lame', '-b:a', '64k', '-map_metadata', '-1', str(output)], input=clip.tobytes(), check=True)
    return signal


def measure(path):
    audio = decode(path)
    first, last = activity(audio)
    step = len(audio)//22
    bins = np.array([np.sqrt(np.mean(audio[i*step:(i+1)*step]**2)) for i in range(22)])
    bars = .12+.88*bins/bins.max()
    trailing = 0
    for bar in bars[::-1]:
        if bar > .13: break
        trailing += 1
    rms = np.array([np.sqrt(np.mean(audio[i:i+WINDOW]**2)) for i in range(0, len(audio), WINDOW)])
    core = rms[rms > max(10**(-45/20), float(rms.max())*.025)]
    return dict(seconds=round(len(audio)/SAMPLE_RATE, 4), leadMS=round(first/SAMPLE_RATE*1000, 2), tailMS=round((len(audio)-last)/SAMPLE_RATE*1000, 2), activeRMSDB=round(float(20*np.log10(np.sqrt(np.mean(core**2)))), 3), peakDB=round(float(20*np.log10(np.max(np.abs(audio)))), 3), trailingFlatBars=trailing, waveform22=[round(float(x), 5) for x in bars])
