"""Lit reading figures: introduced kana only, no romaji, the card's kana in gold, drawn at 3x."""
import html
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import geometry,reading_window,SCALE
from source_data import course,questions,ordered,reading_introductions

ROLES=('source','clean','darkSource','darkClean')

class ReadingArtworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kana=json.loads((ROOT/'source/kana.json').read_text())
        cls.introductions=reading_introductions()
        cls.figures=json.loads((ROOT/'artwork/artwork.json').read_text())['figures']

    def test_windows_retain_the_frame_and_exclude_unintroduced_cells(self):
        for script in ('hira','kata'):
            forms=[c for c in self.kana if c['script']==script]
            for target in forms:
                top,visible=reading_window(target,forms,self.introductions['read-'+target['id']])
                start=max(0,min(target['row']-1,8))
                self.assertEqual(top,start*360)
                self.assertLessEqual({c['row'] for c in visible},set(range(start,start+3)))
                self.assertTrue(all(c['id'] in self.introductions['read-'+target['id']] for c in visible))
                self.assertIn(target,visible)
                for c in visible:
                    x,y,w,h=geometry(c,top)
                    self.assertTrue(0<=x<x+w<=1000 and 0<=y<y+h<=1080)
                # Squares never overlap: each is its own kana's.
                for a in visible:
                    for b in visible:
                        if a!=b:
                            ax,ay,aw,ah=geometry(a,top);bx,by,bw,bh=geometry(b,top)
                            self.assertTrue(ax+aw<=bx or bx+bw<=ax or ay+ah<=by or by+bh<=ay)
            self.assertEqual(reading_window(forms[-1],forms,self.introductions['read-'+forms[-1]['id']])[0],2880)
            self.assertEqual(len(reading_window(forms[-1],forms,self.introductions['read-'+forms[-1]['id']])[1]),8)

    def test_all_92_figures_are_lit_with_one_titled_region_at_the_target_global_ordinal(self):
        for target in self.kana:
            forms=[c for c in self.kana if c['script']==target['script']]
            figure=self.figures['read-'+target['id']]
            start=max(0,min(target['row']-1,8));top=start*360
            visible=[c for c in forms if start<=c['row']<start+3 and c['id'] in self.introductions['read-'+target['id']]]
            def box(c):
                x,y,w,h=geometry(c,top);return [[x/1000,y/1080],[w/1000,h/1080]]
            with self.subTest(target=target['id']):
                self.assertEqual(figure['crop'],{'top':top,'height':1080,'rows':sorted({c['row'] for c in visible})})
                occlusion=figure['occlusion'];preparation=figure['preparation']
                self.assertEqual(occlusion['imageSize'],[3000,3240])
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
                self.assertEqual(figure['visibleKana'],[c['id'] for c in visible])

    def test_lit_names_avoid_collisions_with_every_previous_table_edition(self):
        table_files=set();questions=set()
        for target in self.kana:
            f=self.figures['read-'+target['id']]
            for role in ROLES:
                asset=f[role];table_files.add(asset['file'])
                self.assertEqual((asset['width'],asset['height']),(1000*SCALE,1080*SCALE))
                self.assertNotIn('fonts',asset)
                self.assertTrue(asset['file'].startswith('rv-kana-'+target['id']+'-lit-'))
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
