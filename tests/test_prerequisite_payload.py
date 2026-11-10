"""Each card's payload says what it requires and what it introduces (the app's Lesson mode)."""
import html,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from source_data import inputs

def payloads(language,**options):
 notes=inputs(language,**options)[1]
 return {n['itemId']:json.JSONDecoder().raw_decode(html.unescape(n['fields']['RectoVerso']))[0] for n in notes}

class PrerequisitePayloadTests(unittest.TestCase):
 def test_a_reading_introduces_its_kana_and_requires_its_figures_other_kana(self):
  for language in ['en','fr']:
   p=payloads(language)
   self.assertEqual(p['read-hira-3042'].get('introduces'),['hira-3042'])
   self.assertNotIn('requires',p['read-hira-3042'])
   self.assertEqual(p['read-hira-3044'].get('introduces'),['hira-3044'])
   self.assertEqual(p['read-hira-3044'].get('requires'),['hira-3042'])
 def test_listening_words_and_comparisons_only_require(self):
  p=payloads('en')
  self.assertEqual(p['listen-hira-a'].get('requires'),['hira-3042'])
  self.assertEqual(p['word-ai'].get('requires'),['hira-3042','hira-3044'])
  self.assertEqual(p['contrast-nu-me-nu'].get('requires'),['hira-306c','hira-3081'])
  for item in ['listen-hira-a','word-ai','contrast-nu-me-nu']:self.assertNotIn('introduces',p[item])
 def test_the_decks_order_teaches_before_it_asks(self):
  for language in ['en','fr']:
   for options in [{},{'beginner_trial':True}]:
    taught=set()
    for item,p in payloads(language,**options).items():
     missing=[t for t in p.get('requires',[]) if t not in taught]
     self.assertFalse(missing,f'{language} {options} {item}: {missing}')
     taught.update(p.get('introduces',[]))
 def test_the_trial_requires_only_what_it_introduces(self):
  p=payloads('en',beginner_trial=True)
  self.assertEqual(len(p),20)
  introduced={t for v in p.values() for t in v.get('introduces',[])}
  self.assertTrue(all(set(v.get('requires',[]))<=introduced for v in p.values()))
  self.assertEqual(p['word-ai'].get('requires'),['hira-3042','hira-3044'])
 def test_a_type_preview_declares_nothing(self):
  # A review component alone can't teach what it requires: the app would hold every card back.
  for p in payloads('en',only_type='listening').values():
   self.assertNotIn('requires',p);self.assertNotIn('introduces',p)

if __name__=='__main__':unittest.main()
