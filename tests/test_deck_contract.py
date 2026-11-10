"""rectoverso.json states what the course makes, in the deck kit's shape."""
import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from source_data import course,declared,inputs,made
from metadata import updated

class DeckContractTests(unittest.TestCase):
 def test_rectoverso_json_is_what_metadata_py_writes(self):
  meta=json.loads((ROOT/'rectoverso.json').read_text());self.assertEqual(updated(meta),meta)
 def test_inputs_return_the_declared_metadata_and_the_courses_notes(self):
  for language in ('en','fr'):
   with self.subTest(language=language):
    expanded,notes,types,deck=inputs(language);_,made_notes,models,made_deck=course(language)
    self.assertEqual(expanded,declared(language));self.assertEqual((notes,types,deck),(made_notes,models,made_deck))
    self.assertNotIn('languages',expanded);self.assertEqual(expanded['deckID'],'rectoverso-kana');self.assertEqual(expanded['language'],language)
 def test_every_picture_has_one_credit_under_the_decks_license(self):
  facts=made('en');self.assertEqual(facts['pictures'],len(facts['imageCredits']))
  self.assertEqual({credit['license'] for credit in facts['imageCredits']},{'CC-BY-4.0'})
  self.assertEqual(len({credit['file'] for credit in facts['imageCredits']}),facts['pictures'])
 def test_a_stale_rectoverso_json_is_refused(self):
  import source_data
  real=source_data.read
  def stale(path):
   value=real(path)
   if path=='rectoverso.json':value['cards']+=1
   return value
  source_data.read=stale
  try:
   with self.assertRaises(ValueError):inputs('en')
  finally:source_data.read=real

if __name__=='__main__':unittest.main()
