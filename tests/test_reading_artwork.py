"""Reading cards: the big kana as the question; its row of the chart, filling in, as the answer's picture."""
import html
import json
import re
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import slot,square,row,W,H
from source_data import course,questions,ordered,reading_introductions

class ReadingArtworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kana=json.loads((ROOT/'source/kana.json').read_text())
        cls.introductions=reading_introductions()
        cls.figures=json.loads((ROOT/'artwork/artwork.json').read_text())['figures']

    def test_the_row_is_the_cards_own_row_with_its_romaji(self):
        # Five vowel slots across, the kana over their romaji, about 1,000 pixels wide.
        self.assertEqual((W,H),(1050,268))
        for script in ('hira','kata'):
            forms=[c for c in self.kana if c['script']==script]
            self.assertEqual(len(forms),46)
            # や/ゆ/よ and わ/を in their standard slots, ん alone.
            self.assertEqual({(c['row'],c['column']) for c in forms if c['row'] in (7,9,10)},{(7,0),(7,2),(7,4),(9,0),(9,4),(10,0)})
            for c in forms:
                x,y,w,h=slot(c);sx,sy,sw,sh=square(c)
                self.assertTrue(0<=x<x+w<=W and (y,h)==(0,H))
                self.assertTrue(x<=sx<sx+sw<=x+w and 0<=sy<sy+sh<=H)
            for target in forms:
                with self.subTest(target=target['id']):
                    taught,ghosts=row(target,forms,self.introductions['read-'+target['id']])
                    members=taught+ghosts
                    self.assertEqual({c['row'] for c in members},{target['row']})
                    self.assertEqual(len(members),sum(c['row']==target['row'] for c in forms))
                    self.assertIn(target,taught)
                    figure=self.figures['read-'+target['id']]
                    self.assertEqual(figure['visibleKana'],[c['id'] for c in taught])
                    self.assertEqual(figure['ghostKana'],[c['id'] for c in ghosts])
                    self.assertEqual(set(figure),{'visibleKana','ghostKana','answer','question'})
                    self.assertTrue(all(c['id'] in self.introductions['read-'+target['id']] for c in taught if c!=target))
            # The row fills in: its first card inks one kana, its last the whole row.
            readings=[q for q in ordered(questions()) if q['type']=='reading' and q['target'].startswith(script)]
            first=next(c for c in forms if c['id']==readings[0]['target'])
            self.assertEqual(len(row(first,forms,self.introductions[readings[0]['id']])[0]),1)

    def test_chart_names_avoid_collisions_with_every_previous_table_edition(self):
        charts=set();questions=set()
        for target in self.kana:
            f=self.figures['read-'+target['id']]
            a=f['answer'];charts.add(a['file'])
            self.assertEqual(a['file'],'rv-kana-'+target['id']+'-answer-row.png')
            self.assertEqual((a['width'],a['height']),(W,H))
            q=f['question'];questions.add(q['file'])
            self.assertEqual(q['file'],'rv-kana-'+target['id']+'-question.png')
            self.assertEqual((q['width'],q['height']),(700,500))
        self.assertEqual(len(charts),92)
        self.assertEqual(len(questions),92)

    def test_both_packages_keep_one_note_and_card_per_reading_with_the_row_on_the_answer(self):
        for language in ('en','fr'):
            _,notes,_,_=course(language)
            reading=[n for n in notes if n['itemId'].startswith('read-')]
            self.assertEqual(len(reading),92)
            payloads=[json.JSONDecoder().raw_decode(html.unescape(n['fields']['RectoVerso']))[0] for n in reading]
            self.assertEqual(len({p['card'] for p in payloads}),92)
            self.assertEqual(len({p['noteID'] for p in payloads}),92)
            for n,p in zip(reading,payloads):
                with self.subTest(language=language,note=n['itemId']):
                    f=self.figures[n['itemId']];c=next(k for k in self.kana if 'read-'+k['id']==n['itemId'])
                    self.assertEqual(p['kind'],'basic')
                    self.assertEqual(p['noteID'],n['guid'])
                    for key in ('occlusion','preparation','originalOcclusionAnswer'):self.assertNotIn(key,p)
                    # The question is the big kana alone; the answer is its reading, then its row.
                    self.assertEqual(n['fields']['Front'],'<img src="'+f['question']['file']+'" alt="'+c['kana']+'">')
                    back=n['fields']['Back']
                    self.assertTrue(back.startswith(c['reading']+'<img src="'+f['answer']['file']+'" alt="'),back)
                    self.assertTrue(back.endswith('[sound:'+c['audio']+']'))
                    self.assertEqual(re.findall(r'src="([^"]+)"',n['fields']['RectoVerso']),[])
            self.assertEqual([n['due'] for n in notes],list(range(1,len(notes)+1)))

if __name__=='__main__':unittest.main()
