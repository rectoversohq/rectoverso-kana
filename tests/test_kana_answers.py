import copy
import html
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from source_data import inputs,questions,stable_id
from schema_update import check_schema_update

OLD_FIELDS=['Front','Back','Kicker','Meta','Example','Note','RectoVerso search','RectoVerso']

class KanaAnswerTests(unittest.TestCase):
    def test_all_kana_answers_keep_recordings_and_put_romaji_in_both_detail_formats(self):
        items={q['id']:q for q in questions()}
        for language in ('en','fr'):
            _,notes,models,_=inputs(language);seen=0;single=0;grouped=0
            for note in notes:
                q=items[note['itemId']];f=note['fields']
                native=json.JSONDecoder().raw_decode(html.unescape(f['RectoVerso']))[0]
                if q['type'] in ('listening','contrast'):
                    kana=' / '.join(q['accepted']) if q['type']=='listening' else q['answerKana']
                    self.assertEqual(f['Back'],kana+'[sound:'+q['audio']+']')
                    self.assertEqual(f['Romaji'],q['answerReading'])
                    self.assertEqual(native['resources'],[{'name':'Romaji','text':q['answerReading']}])
                    seen+=1;single+=len(kana)==1;grouped+=len(kana)>1
                else:
                    self.assertEqual(f['Romaji'],'')
                    self.assertNotIn('resources',native)
            self.assertEqual((seen,single,grouped),(106,100,6))
            template=models['kana']['templates'][0]
            self.assertNotIn('Romaji',template['qfmt'])
            self.assertIn('<input type="button"',template['afmt'])
            self.assertIn('id="rv-details" hidden',template['afmt'])
            self.assertIn('<strong>Romaji</strong><br>{{Romaji}}',template['afmt'])
            self.assertIn("getElementById('rv-details')",template['afmt'])

    def test_old_field_names_ids_and_template_identity_stay_before_new_field(self):
        for language in ('en','fr'):
            _,_,models,_=inputs(language);model=models['kana']
            self.assertEqual(model['fields'],OLD_FIELDS+['Romaji'])
            for name in OLD_FIELDS:
                self.assertEqual(model['fieldIDs'][name],stable_id(f'rv-kana/{language}/field/{name}'))
            self.assertEqual(model['templates'][0]['id'],stable_id(f'rv-kana/{language}/template'))

    def test_schema_append_preserves_the_old_prefix(self):
        old={1:([(f,i) for i,f in enumerate(OLD_FIELDS)],[15])}
        new={1:(old[1][0]+[('Romaji',20)],[15])}
        check_schema_update(old,new,new)
        check_schema_update(new,new,new)

    def test_schema_migrations_reject_removal_reorder_changed_ids_and_unexpected_fields(self):
        old={1:([(f,i) for i,f in enumerate(OLD_FIELDS)],[15])}
        good={1:(old[1][0]+[('Romaji',20)],[15])}
        bad=[]
        bad.append({1:(good[1][0][1:],[15])})
        fields=good[1][0].copy();fields[0],fields[1]=fields[1],fields[0];bad.append({1:(fields,[15])})
        fields=good[1][0].copy();fields[0]=('Front',99);bad.append({1:(fields,[15])})
        bad.append({1:(good[1][0],[99])})
        bad.append({2:good[1]})
        bad.append({1:(old[1][0]+[('Other',20)],[15])})
        for value in bad:
            with self.subTest(schema=value),self.assertRaises(ValueError):check_schema_update(old,value,value)
        with self.assertRaises(ValueError):check_schema_update(old,good,old)

if __name__=='__main__':unittest.main()
