"""Write into rectoverso.json what the complete course makes: each language's card count, sample and
package name, the count of pictures and their credits. The deck kit's check (kit/check.py) holds the
file to the course; this keeps the two together after a change to the questions or the artwork.

  python scripts/metadata.py           write rectoverso.json
  python scripts/metadata.py --check   fail if it would change
"""
import json,sys
from source_data import ROOT,made

def updated(meta):
 meta=json.loads(json.dumps(meta));facts={language:made(language) for language in meta['languages']}
 first=next(iter(facts.values()))
 if any((f['cards'],f['pictures'],f['imageCredits'])!=(first['cards'],first['pictures'],first['imageCredits']) for f in facts.values()):raise ValueError('The languages differ in cards or pictures')
 meta.update(cards=first['cards'],pictures=first['pictures'],imageCredits=first['imageCredits'])
 for language,f in facts.items():meta['languages'][language].update(cards=f['cards'],sample=f['sample'],package=f['package'])
 return meta

if __name__=='__main__':
 path=ROOT/'rectoverso.json';meta=json.loads(path.read_text());new=updated(meta)
 if '--check' in sys.argv:
  if new!=meta:sys.exit('rectoverso.json differs from what the course makes: run scripts/metadata.py')
 else:path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
