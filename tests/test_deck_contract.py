"""rectoverso.json states what the course makes, in the deck kit's shape."""
import html,json,sys,unittest
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

 def test_the_book_is_the_id_rectoverso_gives_the_packages_anki_deck(self):
  # RectoVerso's gallery knows a deck on the shelf by the id it derives from the package's Anki
  # deck; a payload's book must be that id, or the gallery offers Get for a deck already there.
  # The literals are the app's own function's (UUID(stableFrom: "anki/deck/<id>")), run on these ids.
  expected={('en',False):(1794200000,'bd81281a-a7b7-d960-0ef1-3a98d67765f1'),('fr',False):(1794200100,'c4e4631a-ab8a-a8ab-05da-ff98d1330226'),('en',True):(1794202000,'2768a02c-8dc6-ce82-241b-12a84886cf33')}
  for (language,trial),(deck_id,book) in expected.items():
   with self.subTest(language=language,trial=trial):
    meta,notes,_,deck=course(language,beginner_trial=trial)
    self.assertEqual(deck['id'],deck_id);self.assertEqual(meta['bookUUID'],book)
    self.assertEqual({json.JSONDecoder().raw_decode(html.unescape(note['fields']['RectoVerso']))[0]['book'] for note in notes},{book})

if __name__=='__main__':unittest.main()
