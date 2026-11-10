"""Actual prompt glyphs, not authored requires alone, protect the beginner trial."""
import copy,sys,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from source_data import inputs,questions

class IntroductionGuardTests(unittest.TestCase):
 def test_word_with_an_undeclared_unintroduced_kana_is_rejected(self):
  items=copy.deepcopy(questions())
  next(q for q in items if q['id']=='word-ai')['display']='あさ'
  with patch('source_data.questions',return_value=items):
   with self.assertRaisesRegex(ValueError,'Unintroduced kana'):
    inputs('en',beginner_trial=True)
 def test_reading_figure_cannot_show_an_untaught_neighbor(self):
  import json
  art=json.loads((ROOT/'artwork/artwork.json').read_text());forms=json.loads((ROOT/'source/kana.json').read_text())
  art['figures']['read-hira-3042']['visibleKana'].append('hira-3044')
  with self.assertRaisesRegex(ValueError,'Unintroduced kana'):
   inputs('en',artwork=art,beginner_trial=True)

if __name__=='__main__':unittest.main()
