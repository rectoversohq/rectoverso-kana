"""Reading cards: the big kana as the question; the whole chart, filling in, as the answer's picture."""
import html
import json
import re
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import geometry,chart,W,H
from source_data import course,questions,ordered,reading_introductions

class ReadingArtworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kana=json.loads((ROOT/'source/kana.json').read_text())
        cls.introductions=reading_introductions()
        cls.figures=json.loads((ROOT/'artwork/artwork.json').read_text())['figures']

    def test_the_chart_is_the_whole_gojuon_on_its_side(self):
        # Eleven consonant columns by five vowel rows, about 1,000 pixels wide.
        self.assertEqual((W,H),(1040,488))
        for script in ('hira','kata'):
            forms=[c for c in self.kana if c['script']==script]
            self.assertEqual(len(forms),46)
            # や/ゆ/よ and わ/を in their standard cells, ん on its own.
            self.assertEqual({(c['row'],c['column']) for c in forms if c['row'] in (7,9,10)},{(7,0),(7,2),(7,4),(9,0),(9,4),(10,0)})
            for c in forms:
                x,y,w,h=geometry(c)
                self.assertTrue(0<=x<x+w<=W and 0<=y<y+h<=H)
            for a in forms:
                for b in forms:
                    if a!=b:
                        ax,ay,aw,ah=geometry(a);bx,by,bw,bh=geometry(b)
                        self.assertTrue(ax+aw<=bx or bx+bw<=ax or ay+ah<=by or by+bh<=ay)
                        # Its consonant's column, left to right; its vowel's row, top to bottom.
                        if a['row']<b['row']:self.assertLess(ax,bx)
                        if a['row']==b['row'] and a['column']<b['column']:self.assertLess(ay,by)
            # The chart fills in: the first card inks one kana, the last its whole script.
            readings=[q for q in ordered(questions()) if q['type']=='reading' and q['target'].startswith(script)]
            target=lambda q:next(c for c in forms if c['id']==q['target'])
            self.assertEqual(len(chart(target(readings[0]),forms,self.introductions[readings[0]['id']])[0]),1)
            self.assertEqual(len(chart(target(readings[-1]),forms,self.introductions[readings[-1]['id']])[1]),0)

    def test_all_92_charts_ink_what_the_card_has_taught(self):
        for target in self.kana:
            forms=[c for c in self.kana if c['script']==target['script']]
            figure=self.figures['read-'+target['id']]
            taught=[c for c in forms if c['id'] in self.introductions['read-'+target['id']]]
            with self.subTest(target=target['id']):
                self.assertIn(target,taught)
                self.assertEqual(figure['visibleKana'],[c['id'] for c in taught])
                self.assertEqual(figure['ghostKana'],[c['id'] for c in forms if c not in taught])
                self.assertEqual(set(figure),{'visibleKana','ghostKana','answer','question'})

    def test_chart_names_avoid_collisions_with_every_previous_table_edition(self):
        charts=set();questions=set()
        for target in self.kana:
            f=self.figures['read-'+target['id']]
            a=f['answer'];charts.add(a['file'])
            self.assertEqual(a['file'],'rv-kana-'+target['id']+'-answer-chart.png')
            self.assertEqual((a['width'],a['height']),(W,H))
            q=f['question'];questions.add(q['file'])
            self.assertEqual(q['file'],'rv-kana-'+target['id']+'-question.png')
            self.assertEqual((q['width'],q['height']),(700,500))
        self.assertEqual(len(charts),92)
        self.assertEqual(len(questions),92)

    def test_both_packages_keep_one_note_and_card_per_reading_with_the_chart_on_the_answer(self):
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
                    # The question is the big kana alone; the answer is its reading, then the chart.
                    self.assertEqual(n['fields']['Front'],'<img src="'+f['question']['file']+'" alt="'+c['kana']+'">')
                    back=n['fields']['Back']
                    self.assertTrue(back.startswith(c['reading']+'<img src="'+f['answer']['file']+'" alt="'),back)
                    self.assertTrue(back.endswith('[sound:'+c['audio']+']'))
                    self.assertEqual(re.findall(r'src="([^"]+)"',n['fields']['RectoVerso']),[])
            self.assertEqual([n['due'] for n in notes],list(range(1,len(notes)+1)))

if __name__=='__main__':unittest.main()
