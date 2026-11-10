"""Checks at the shared source/package boundary, independent of rendering."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from source_data import ROOT, ordered, questions
from font_sources import font_path

TYPES = ('reading','listening','rule','word','contrast','variant','checkpoint')

def check_questions(items, kana, references):
    ids=[q['id'] for q in items]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate question identity')
    for q in items:
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',q['id']):raise ValueError('Malformed question identity: '+q['id'])
        if q['type'] not in TYPES:raise ValueError('Unknown question type')
        for field in ['instruction','note']:
            if set(q[field])!={'en','fr'} or not all(q[field].values()):raise ValueError('Incomplete bilingual '+field)
            if any('\\u' in text for text in q[field].values()):raise ValueError('Literal Unicode escape in prose')
        if not set(q['references'])<=references:raise ValueError('Unknown primary reference: '+q['id'])
        if q['type'] in ['rule','word','checkpoint']:
            if not re.fullmatch(r'[\u3040-\u30ff\u3000\s]+',q['display']):raise ValueError('Non-kana decoding front')
        if q['type']=='listening' and ('answerReading' not in q or not q['accepted']):raise ValueError('Incomplete listening answer')
    sequence=ordered(items)
    positions={token:i for i,q in enumerate(sequence) for token in q.get('introduces',[])}
    for i,q in enumerate(sequence):
        if q['type']=='listening' and any(i-positions[token]<2 for token in q['requires']):
            raise ValueError('Reverse question immediately follows its reading: '+q['id'])
    reading=[q for q in items if q['type']=='reading']
    if reading and Counter(q['target'] for q in reading)!=Counter(c['id'] for c in kana):raise ValueError('Basic reading inventory differs')
    listening=[q for q in items if q['type']=='listening']
    if listening:
        for script in ['hira','kata']:
            groups={sound:{c['kana'] for c in kana if c['script']==script and c['reading']==sound} for sound in {c['reading'] for c in kana if c['script']==script}}
            actual=[q for q in listening if q['id'].startswith('listen-'+script+'-') and q.get('scope')!='application']
            if len(actual)!=45:raise ValueError('Sound grouping count differs')
            if {q['answerReading']:set(q['accepted']) for q in actual}!=groups:raise ValueError('Sound grouping differs from forms')
            for q in actual:
                expected={c['id'] for c in kana if c['script']==script and c['reading']==q['answerReading']}
                if set(q['requires'])!=expected:raise ValueError('Listening prerequisites differ from accepted forms')
    teaching=set(re.findall(r'[\u3040-\u30ff]+','\n'.join(q.get('display','')+'\n'+'\n'.join(q['note'].values()) for q in items if q['type']!='checkpoint')))
    for q in items:
        if q['type']=='checkpoint' and q['display'] in teaching:raise ValueError('Checkpoint word was already taught: '+q['id'])
    for q in listening:
        if q.get('scope')=='application':
            script='hira' if '-hira-' in q['id'] else 'kata'
            accepted={'ji':['じ','ぢ'],'zu':['ず','づ']}[q['answerReading']]
            if script=='kata':accepted=[chr(ord(c)+0x60) for c in accepted]
            if q['accepted']!=accepted or set(q['requires'])!={script+'-marks-z',script+'-marks-d'}:raise ValueError('Marked shared-sound application differs')
    for i in range(len(sequence)-3):
        if sum(q['type']=='reading' for q in sequence[i:i+4])>2:
            raise ValueError('More than two new basic kana in four consecutive questions')
    return sequence

def check_audio(root=ROOT):
    directory=root/'source/audio'
    provenance=json.loads((directory/'provenance.json').read_text())
    records={r['file']:r for r in provenance}
    if len(records)!=len(provenance):raise ValueError('Duplicate audio provenance')
    for name,r in records.items():
        if Path(name).name!=name or not name.endswith('.mp3'):raise ValueError('Unsafe audio name')
        if r['voice']!='ja-JP-NanamiNeural' or r['rate']!='-20%':raise ValueError('Unapproved voice or pace')
        if hashlib.sha256((directory/name).read_bytes()).hexdigest()!=r['sha256']:raise ValueError('Audio digest differs: '+name)
    return records

def check_study(metadata):
    expected={'newCards':'deckOrder','newPerDay':4,'newPosition':'afterReviews'}
    study=metadata.get('study')
    if study!=expected or type(study['newPerDay']) is not int:
        raise ValueError('Study preset differs from the owner-approved course settings')
    if 'studyRecommendations' in metadata:
        raise ValueError('Legacy studyRecommendations must be replaced by study')

def check_source(root=ROOT):
    check_study(json.loads((root/'rectoverso.json').read_text()))
    items=questions();kana=json.loads((root/'source/kana.json').read_text())
    refs={r['id'] for r in json.loads((root/'source/references.json').read_text())}
    sequence=check_questions(items,kana,refs);audio=check_audio(root)
    for font in json.loads((root/'artwork/fonts/provenance.json').read_text()):
        font_path(font['file'], root)
    if {p.name for p in (root/'source/audio').glob('*.mp3')}!=set(audio):raise ValueError('Unrecorded source audio')
    for q in items:
        name=(next(c['audio'] for c in kana if c['id']==q['target']) if q['type']=='reading' else q['audio'])
        if name not in audio:raise ValueError('Missing audio provenance: '+q['id'])
    return dict(cards=len(items),types=dict(Counter(q['type'] for q in items)),audioFiles=len(audio),sequence=[q['id'] for q in sequence],status='pass')
