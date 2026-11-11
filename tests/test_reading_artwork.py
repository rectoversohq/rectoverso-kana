"""Reading figures: the whole chart, taught kana in ink, the rest ghosts, the card's kana in gold, drawn at 3x."""
import html
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import geometry,chart,SCALE,W,H
from source_data import course,questions,ordered,reading_introductions

ROLES=('source','clean','darkSource','darkClean')

class ReadingArtworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kana=json.loads((ROOT/'source/kana.json').read_text())
        cls.introductions=reading_introductions()
        cls.figures=json.loads((ROOT/'artwork/artwork.json').read_text())['figures']

    def test_the_chart_is_the_whole_gojuon_and_its_squares_fill_it(self):
        self.assertEqual((W,H),(940,2020))
        for script in ('hira','kata'):
            forms=[c for c in self.kana if c['script']==script]
            self.assertEqual(len(forms),46)
            # や/ゆ/よ and わ/を in their standard cells, ん on its own row.
            self.assertEqual({(c['row'],c['column']) for c in forms if c['row'] in (7,9,10)},{(7,0),(7,2),(7,4),(9,0),(9,4),(10,0)})
            for c in forms:
                x,y,w,h=geometry(c)
                self.assertTrue(0<=x<x+w<=W and 0<=y<y+h<=H)
            for a in forms:
                for b in forms:
                    if a!=b:
                        ax,ay,aw,ah=geometry(a);bx,by,bw,bh=geometry(b)
                        self.assertTrue(ax+aw<=bx or bx+bw<=ax or ay+ah<=by or by+bh<=ay)
            # The chart fills in: the first card shows one kana in ink, the last its whole script.
            first=next(q for q in ordered(questions()) if q['type']=='reading' and q['target'].startswith(script))
            last=[q for q in ordered(questions()) if q['type']=='reading' and q['target'].startswith(script)][-1]
            target=lambda q:next(c for c in forms if c['id']==q['target'])
            self.assertEqual(len(chart(target(first),forms,self.introductions[first['id']])[0]),1)
            self.assertEqual(len(chart(target(last),forms,self.introductions[last['id']])[1]),0)

    def test_all_92_figures_are_lit_with_one_titled_region_at_the_target_global_ordinal(self):
        for target in self.kana:
            forms=[c for c in self.kana if c['script']==target['script']]
            figure=self.figures['read-'+target['id']]
            taught=[c for c in forms if c['id'] in self.introductions['read-'+target['id']]]
            def box(c):
                x,y,w,h=geometry(c);return [[x/W,y/H],[w/W,h/H]]
            with self.subTest(target=target['id']):
                self.assertIn(target,taught)
                self.assertEqual(figure['visibleKana'],[c['id'] for c in taught])
                self.assertEqual(figure['ghostKana'],[c['id'] for c in forms if c not in taught])
                self.assertNotIn('crop',figure)
                occlusion=figure['occlusion'];preparation=figure['preparation']
                self.assertEqual(occlusion['imageSize'],[W*SCALE,H*SCALE])
                self.assertEqual(occlusion['ordinal'],forms.index(target)+1)
                self.assertEqual(occlusion['box'],box(target))
                self.assertEqual(occlusion['label'],target['reading'])
                self.assertEqual(occlusion['mode'],'hideAll')
                self.assertEqual(occlusion['siblings'],[])
                self.assertEqual(preparation['mode'],'lit')
                self.assertEqual(preparation['masksSHA256'],'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
                self.assertEqual(preparation['regions'],[{'id':target['id'],'ordinal':forms.index(target)+1,'kind':'label','geometry':{'kind':'rect','coordinates':sum(box(target),[])},'answer':target['reading'],'title':target['reading']}])
                self.assertEqual(occlusion['imageName'],figure['source']['file'])
                for role in ROLES:self.assertEqual(preparation[role],figure[role])

    def test_chart_names_avoid_collisions_with_every_previous_table_edition(self):
        table_files=set();questions=set()
        for target in self.kana:
            f=self.figures['read-'+target['id']]
            for role in ROLES:
                asset=f[role];table_files.add(asset['file'])
                self.assertEqual((asset['width'],asset['height']),(W*SCALE,H*SCALE))
                self.assertNotIn('fonts',asset)
                self.assertTrue(asset['file'].startswith('rv-kana-'+target['id']+'-chart-'))
            q=f['question'];questions.add(q['file'])
            self.assertEqual(q['file'],'rv-kana-'+target['id']+'-question.png')
            self.assertEqual((q['width'],q['height']),(700,500))
        self.assertEqual(len(table_files),368)
        self.assertEqual(len(questions),92)

    def test_both_packages_keep_one_note_and_native_card_per_reading(self):
        for language in ('en','fr'):
            _,notes,_,_=course(language)
            reading=[n for n in notes if n['itemId'].startswith('read-')]
            self.assertEqual(len(reading),92)
            payloads=[json.JSONDecoder().raw_decode(html.unescape(n['fields']['RectoVerso']))[0] for n in reading]
            self.assertEqual(len({p['card'] for p in payloads}),92)
            self.assertEqual(len({p['noteID'] for p in payloads}),92)
            self.assertEqual(len({json.dumps(p['preparation'],sort_keys=True) for p in payloads}),92)
            for n,p in zip(reading,payloads):
                self.assertEqual(p['noteID'],n['guid'])
                self.assertEqual(p['occlusion'],self.figures[n['itemId']]['occlusion'])
            self.assertEqual([n['due'] for n in notes],list(range(1,len(notes)+1)))

if __name__=='__main__':unittest.main()
