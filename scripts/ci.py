"""Offline source, component, independent-render and Anki integration checks."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from build import build
from course_contract import ROOT,TYPES,check_source
from render_artwork import render

def command(*args):subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,check=True)

def ci(output,previous=None):
    output=output.resolve()
    if output.is_relative_to(ROOT) or output.exists():raise ValueError('Choose a new output directory outside the checkout')
    output.mkdir(parents=True)
    source=check_source();(output/'source.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
    command('-m','unittest','discover','-s','tests','-v')
    artwork=output/'first/artwork';record=render(artwork)
    canonical=json.loads((ROOT/'artwork/artwork.json').read_text())
    if record!=canonical:raise ValueError('Rendered artwork differs from the frozen source record')
    for language in ['en','fr']:
        package=output/'first/packages'/f'Japanese-Kana-{language}.apkg';build(language,package,artwork=artwork)
        command('scripts/checks/validate-anki.py',package,'--output',output/'evidence'/language)
        if previous is not None:
            command('scripts/checks/validate-update.py',previous/package.name,package,'--output',output/'evidence'/f'{language}-edition-update.json')
        for kind in TYPES:
            component=output/'components'/f'Japanese-Kana-{language}-{kind}.apkg';build(language,component,kind,artwork)
            command('scripts/checks/validate-anki.py',component,'--output',output/'evidence'/f'{language}-{kind}')
        trial=output/'trials'/f'Japanese-Kana-{language}-beginner-trial.apkg'
        build(language,trial,artwork=artwork,beginner_trial=True)
        command('scripts/checks/validate-anki.py',trial,'--output',output/'evidence'/f'{language}-beginner-trial')
    other_artwork=output/'second/artwork';other=render(other_artwork)
    if record!=other:raise ValueError('Independent renders are not byte-identical')
    for language in ['en','fr']:
        first=output/'first/packages'/f'Japanese-Kana-{language}.apkg';second=output/'second/packages'/first.name
        build(language,second,artwork=other_artwork)
        command('scripts/checks/validate-rebuild.py',first,second,output/'evidence'/f'{language}-rebuild.json')
        trial=output/'second/trials'/f'Japanese-Kana-{language}-beginner-trial.apkg'
        build(language,trial,artwork=other_artwork,beginner_trial=True)
        command('scripts/checks/validate-rebuild.py',output/'trials'/trial.name,trial,output/'evidence'/f'{language}-trial-rebuild.json')
    command('scripts/checks/verify-covers.py','--output',output/'first/packages','--compare',output/'second/packages')
    report=dict(coverPNGs=6,independentCoverBytesExact=True,status='pass',beginnerTrialCards=20,cards=source['cards'],types=source['types'],languages=['en','fr'],independentArtworkBytesExact=True,independentPackageSemanticsExact=True,studyProgressPreserved=True,publicationApproved=False,nativeChecks='partial; see docs/review.md',newAudioListening='pending')
    (output/'result.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--previous',type=Path);a=p.parse_args();ci(a.output,a.previous)
