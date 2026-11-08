"""Beginner introduction density and existing prerequisites."""
import copy,json,sys,unittest
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from source_data import ordered,questions,reading_introductions
from course_contract import check_questions

class GentleSequenceTests(unittest.TestCase):
 def setUp(self):self.items=questions();self.sequence=ordered(self.items)
 def test_first_two_days_are_two_readings_then_their_two_listening_questions(self):
  self.assertEqual([q['id'] for q in self.sequence[:8]],['read-hira-3042','read-hira-3044','listen-hira-a','listen-hira-i','read-hira-3046','read-hira-3048','listen-hira-u','listen-hira-e'])
 def test_every_rolling_four_questions_introduces_at_most_two_basic_kana(self):
  for start in range(len(self.sequence)-3):
   with self.subTest(start=start):self.assertLessEqual(sum(q['type']=='reading' for q in self.sequence[start:start+4]),2)
  self.assertEqual(Counter(q['batch'] for q in self.sequence if q['type']=='reading'),Counter({script+'-batch-'+str(i).zfill(2):2 for script in ('hira','kata') for i in range(1,24)}))
 def test_pacing_check_rejects_three_readings_in_a_rolling_window(self):
  items=copy.deepcopy(self.items)
  for q in items:
   if q['id']=='read-hira-3046':q['priority']=11
  kana=json.loads((ROOT/'source/kana.json').read_text());refs={r['id'] for r in json.loads((ROOT/'source/references.json').read_text())}
  with self.assertRaisesRegex(ValueError,'More than two'):check_questions(items,kana,refs)
 def test_grouped_o_waits_for_both_spellings_and_the_early_gap_uses_known_word_practice(self):
  for script,first,second in [('hira','hira-304a','hira-3092'),('kata','kata-30aa','kata-30f2')]:
   positions={q['id']:i for i,q in enumerate(self.sequence)}
   self.assertGreater(positions['listen-'+script+'-o'],positions['read-'+second])
  positions={q['id']:i for i,q in enumerate(self.sequence)}
  self.assertLess(positions['read-kata-30ab'],positions['word-hon'])
  self.assertLess(positions['word-hon'],positions['listen-kata-ka'])
  known=set()
  for q in self.sequence:
   self.assertLessEqual(set(q['requires']),known,q['id']);known.update(q.get('introduces',[]))
 def test_first_figures_do_not_include_a_future_member_of_the_same_pair(self):
  introduced=reading_introductions(self.items)
  self.assertEqual(introduced['read-hira-3042'],{'hira-3042'})
  self.assertEqual(introduced['read-hira-3044'],{'hira-3042','hira-3044'})
  self.assertNotIn('hira-3046',introduced['read-hira-3044'])
  self.assertNotIn('kata-30a4',introduced['read-kata-30a2'])

if __name__=='__main__':unittest.main()
