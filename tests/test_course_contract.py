import copy
import json
import sys
import unittest
import os
from unittest.mock import patch
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from course_contract import check_questions,check_source,check_study
from source_data import inputs,questions
from font_sources import font_path

class CourseContractTests(unittest.TestCase):
    def setUp(self):
        self.items=questions()
        self.kana=json.loads((ROOT/'source/kana.json').read_text())
        self.refs={r['id'] for r in json.loads((ROOT/'source/references.json').read_text())}

    def check(self,items):return check_questions(items,self.kana,self.refs)

    def test_actual_source_has_no_dependency_or_audio_drift(self):
        self.assertEqual(check_source()['status'],'pass')

    def test_external_font_override_cannot_silently_substitute_another_face(self):
        with patch.dict(os.environ, {'RECTOVERSO_SF_PRO_FONT': str(ROOT/'artwork/fonts/NotoSansJP.ttf')}):
            with self.assertRaisesRegex(ValueError, 'Pinned font digest differs: SF-Pro'):
                font_path('SF-Pro-Text-Regular.otf')

    def test_missing_external_font_fails_instead_of_falling_back(self):
        with patch.dict(os.environ, {'RECTOVERSO_SF_PRO_FONT': str(ROOT/'artwork/fonts/missing-sf-pro.otf')}):
            with self.assertRaisesRegex(ValueError, 'Missing pinned font SF-Pro'):
                font_path('SF-Pro-Text-Regular.otf')

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

    def test_listening_questions_have_sound_only_front_and_explicit_context(self):
        items={q['id']:q for q in self.items if q['type']=='listening'}
        self.assertEqual(len(items),94)
        for language,hint in [('en','Recall one valid form.'),('fr','Une forme suffit.')]:
            _,notes,_,_=inputs(language)
            listening=[n for n in notes if n['itemId'] in items]
            self.assertEqual(len(listening),94)
            for note in listening:
                question=items[note['itemId']];fields=note['fields']
                with self.subTest(language=language,item=note['itemId']):
                    self.assertEqual(fields['Front'],'[sound:'+question['audio']+']')
                    self.assertEqual(fields['Kicker'],question['instruction'][language])
                    self.assertEqual(fields['Meta'],hint if len(question['accepted'])>1 else '')
                    self.assertEqual(fields['Back'],' / '.join(question['accepted'])+' · '+question['answerReading']+'[sound:'+question['audio']+']')

    def test_owner_approved_play_label_is_kept_in_both_expansions(self):
        labels={'en':'Listen','fr':'Écouter'}
        self.assertEqual(json.loads((ROOT/'rectoverso.json').read_text())['playLabel'],labels)
        for language in labels:
            metadata,_,_,_=inputs(language)
            self.assertEqual(metadata['playLabel'],labels)

    def test_owner_study_preset_is_shared_by_both_language_expansions(self):
        expected={'newCards':'deckOrder','newPerDay':6,'newPosition':'afterReviews'}
        metadata=json.loads((ROOT/'rectoverso.json').read_text())
        check_study(metadata)
        for language in ('en','fr'):
            expanded,notes,_,_=inputs(language)
            self.assertEqual(expanded['study'],expected)
            self.assertNotIn('studyRecommendations',expanded)
            self.assertEqual([n['due'] for n in notes],list(range(1,291)))

    def test_missing_or_drifted_study_preset_is_refused(self):
        preset={'newCards':'deckOrder','newPerDay':6,'newPosition':'afterReviews'}
        for study in (None,{},preset|{'newCards':'random'},preset|{'newPosition':'beforeReviews'},preset|{'newPerDay':20},preset|{'newPerDay':6.0},preset|{'newOrder':'authored'}):
            with self.subTest(study=study),self.assertRaisesRegex(ValueError,'Study preset'):
                check_study({'study':study})

    def test_old_advisory_metadata_cannot_silently_replace_study(self):
        preset={'newCards':'deckOrder','newPerDay':6,'newPosition':'afterReviews'}
        with self.assertRaisesRegex(ValueError,'Legacy studyRecommendations'):
            check_study({'study':preset,'studyRecommendations':{}})

    def test_comparisons_keep_their_text_prompt_and_recording(self):
        items={q['id']:q for q in self.items if q['type']=='contrast'}
        for language in ['en','fr']:
            _,notes,_,_=inputs(language)
            for note in notes:
                if note['itemId'] not in items:continue
                question=items[note['itemId']];fields=note['fields']
                with self.subTest(language=language,item=note['itemId']):
                    self.assertEqual(fields['Front'],question['display']+'[sound:'+question['audio']+']')
                    self.assertEqual(fields['Kicker'],question['instruction'][language])
                    self.assertEqual(fields['Meta'],'')

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
