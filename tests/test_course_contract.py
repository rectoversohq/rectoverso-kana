import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from course_contract import check_questions,check_source
from source_data import inputs,questions

class CourseContractTests(unittest.TestCase):
    def setUp(self):
        self.items=questions()
        self.kana=json.loads((ROOT/'source/kana.json').read_text())
        self.refs={r['id'] for r in json.loads((ROOT/'source/references.json').read_text())}

    def check(self,items):return check_questions(items,self.kana,self.refs)

    def test_actual_source_has_no_dependency_or_audio_drift(self):
        self.assertEqual(check_source()['status'],'pass')

    def test_duplicate_identity_is_refused(self):
        items=copy.deepcopy(self.items);items[1]['id']=items[0]['id']
        with self.assertRaisesRegex(ValueError,'Duplicate'):self.check(items)

    def test_missing_prerequisite_is_refused(self):
        items=copy.deepcopy(self.items);items[-1]['requires'].append('not-introduced')
        with self.assertRaisesRegex(ValueError,'Missing or cyclic'):self.check(items)

    def test_reverse_cannot_follow_its_answer_immediately(self):
        items=copy.deepcopy(self.items);next(q for q in items if q['id']=='listen-hira-a')['priority']=-1000
        with self.assertRaisesRegex(ValueError,'immediately follows'):self.check(items)

    def test_grouped_sound_requires_every_accepted_form(self):
        items=copy.deepcopy(self.items);next(q for q in items if q['id']=='listen-hira-o')['requires']=['hira-304a']
        with self.assertRaisesRegex(ValueError,'prerequisites differ'):self.check(items)

    def test_wrong_sound_group_is_refused(self):
        items=copy.deepcopy(self.items);next(q for q in items if q['id']=='listen-hira-o')['accepted']=['お','か']
        with self.assertRaisesRegex(ValueError,'Sound grouping differs'):self.check(items)

    def test_word_context_cannot_supply_cognate_reading_on_front(self):
        for lang in ['en','fr']:
            _,notes,_,_=inputs(lang)
            by={n['itemId']:n for n in notes}
            for id in ['word-sushi','word-memo','word-tomato']:
                fields=by[id]['fields']
                self.assertEqual(fields['Meta'],'')
                self.assertNotIn('[sound:',fields['Front'])
                self.assertTrue(fields['Example'])

    def test_checkpoint_cannot_reuse_a_taught_word(self):
        items=copy.deepcopy(self.items);next(q for q in items if q['id']=='check-asa')['display']='ねこ'
        with self.assertRaisesRegex(ValueError,'already taught'):self.check(items)

    def test_literal_unicode_escape_in_prose_is_refused(self):
        items=copy.deepcopy(self.items);items[0]['note']['fr']+=' \\u202f'
        with self.assertRaisesRegex(ValueError,'Literal Unicode'):self.check(items)

if __name__=='__main__':unittest.main()
