"""Beginner trial is the reviewed opening with isolated study identities."""
import html,json,sys,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from source_data import course,questions,ordered

class BeginnerTrialTests(unittest.TestCase):
 def test_exact_opening_and_complete_prerequisites(self):
  expected=[q['id'] for q in ordered(questions())[:20]]
  for language in ('en','fr'):
   m,notes,models,deck=course(language,beginner_trial=True)
   self.assertEqual([n['itemId'] for n in notes],expected)
   self.assertEqual(Counter(n['tags'][0] for n in notes),{'exercise::reading':8,'exercise::listening':7,'exercise::word':5})
   self.assertEqual([n['due'] for n in notes],list(range(1,21)))
   self.assertEqual(m['study'],{'newCards':'deckOrder','newPerDay':4,'newPosition':'afterReviews'})
   self.assertNotIn('listen-hira-o',expected)
 def test_trial_cannot_replace_full_course_or_type_previews(self):
  for language in ('en','fr'):
   m,notes,models,deck=course(language,beginner_trial=True)
   for component in (None,'reading','listening','rule','word','contrast','variant','checkpoint'):
    other,others,other_models,other_deck=course(language,only_type=component)
    self.assertNotEqual(m['bookUUID'],other['bookUUID'])
    self.assertNotEqual(deck['id'],other_deck['id'])
    self.assertNotEqual(models['kana']['id'],other_models['kana']['id'])
    self.assertTrue({n['guid'] for n in notes}.isdisjoint(n['guid'] for n in others))
 def test_prompts_answers_media_and_regions_are_unchanged(self):
  for language in ('en','fr'):
   _,full,_,_=course(language);_,trial,_,_=course(language,beginner_trial=True)
   for before,after in zip(full,trial):
    for field in ('Front','Back','Kicker','Meta','Example','Romaji','RectoVerso search'):
     self.assertEqual(before['fields'][field],after['fields'][field])
    a=json.JSONDecoder().raw_decode(html.unescape(before['fields']['RectoVerso']))[0]
    b=json.JSONDecoder().raw_decode(html.unescape(after['fields']['RectoVerso']))[0]
    for key in ('book','card','noteID'):self.assertNotEqual(a.pop(key),b.pop(key))
    self.assertEqual(a,b)
    if before['itemId']!='read-hira-3042':self.assertEqual(before['fields']['Note'],after['fields']['Note'])
 def test_only_trial_guidance_replaces_full_course_promise(self):
  for language,word in [('en','Beginner trial'),('fr','Essai débutant')]:
   m,notes,_,deck=course(language,beginner_trial=True)
   self.assertIn(word,deck['name']);self.assertIn(word,html.unescape(notes[0]['fields']['Note']))
   self.assertNotIn('katakana',m['description'].lower())
   self.assertTrue(all('katakana' not in text.lower() for text in m['headline'].values()))
   self.assertEqual(m['package']['file'],f'Japanese-Kana-{language}-beginner-trial.apkg')
   self.assertEqual(len(notes),20)
 def test_trial_and_type_filters_cannot_be_combined(self):
  with self.assertRaises(ValueError):course('en',only_type='reading',beginner_trial=True)

if __name__=='__main__':unittest.main()
