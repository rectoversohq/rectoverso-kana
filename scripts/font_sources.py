"""Resolve pinned font inputs; proprietary fonts remain locally installed."""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def font_path(name, root=ROOT):
    record = next(r for r in json.loads((root/'artwork/fonts/provenance.json').read_text()) if r['file'] == name)
    path = (Path(os.environ.get(record['environment'], record['defaultPath'])).expanduser()
            if record.get('external') else root/'artwork/fonts'/name)
    if not path.is_file():
        raise ValueError(f"Missing pinned font {name}; install it locally or set {record.get('environment', 'the source font path')}")
    if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
        raise ValueError('Pinned font digest differs: '+name)
    return path
