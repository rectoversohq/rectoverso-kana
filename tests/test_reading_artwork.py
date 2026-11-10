"""Gold-preserving reading figures containing only introduced kana."""
import html
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import geometry,reading_window,ROMAJI_SIZE,font
from source_data import inputs,questions,ordered,reading_introductions

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
            self.assertEqual(reading_window(forms[-1],forms,self.introductions['read-'+forms[-1]['id']])[0],2880)
            self.assertEqual(len(reading_window(forms[-1],forms,self.introductions['read-'+forms[-1]['id']])[1]),8)

    def test_all_92_figures_keep_target_global_ordinal_and_hide_every_visible_reading(self):
        for target in self.kana:
            forms=[c for c in self.kana if c['script']==target['script']]
            figure=self.figures['read-'+target['id']]
            start=max(0,min(target['row']-1,8));top=start*360
            visible=[c for c in forms if start<=c['row']<start+3 and c['id'] in self.introductions['read-'+target['id']]]
            def box(c):return [[(83+176*c['column'])/1000,(223+360*c['row']-top)/1080],[.13,70/1080]]
            with self.subTest(target=target['id']):
                self.assertEqual(figure['crop'],{'top':top,'height':1080,'rows':sorted({c['row'] for c in visible})})
                occlusion=figure['occlusion'];preparation=figure['preparation']
                self.assertEqual(occlusion['imageSize'],[1000,1080])
                self.assertEqual(occlusion['ordinal'],forms.index(target)+1)
                self.assertEqual(occlusion['box'],box(target))
                self.assertEqual(occlusion['label'],target['reading'])
                self.assertEqual(occlusion['mode'],'hideAll')
                self.assertEqual(preparation['mode'],'hideAll')
                self.assertEqual(occlusion['siblings'],[{'rect':{'_0':box(c)}} for c in visible if c!=target])
                self.assertEqual(preparation['regions'],[{'id':c['id'],'ordinal':forms.index(c)+1,'kind':'label','geometry':{'kind':'rect','coordinates':sum(box(c),[])},'answer':c['reading']} for c in visible])
                self.assertEqual(occlusion['imageName'],figure['source']['file'])
                for role in ROLES:self.assertEqual(preparation[role],figure[role])

    def test_progressive_names_avoid_collisions_with_both_previous_table_editions(self):
        table_files=set();questions=set()
        for target in self.kana:
            f=self.figures['read-'+target['id']]
            for role in ROLES:
                asset=f[role];table_files.add(asset['file'])
                self.assertEqual((asset['width'],asset['height']),(1000,1080))
                self.assertIn('-introduced-',asset['file'])
                self.assertTrue(asset['file'].startswith('rv-kana-'+target['id']+'-introduced-'))
            q=f['question'];questions.add(q['file'])
            self.assertEqual(q['file'],'rv-kana-'+target['id']+'-question.png')
            self.assertEqual((q['width'],q['height']),(700,500))
        self.assertEqual(len(table_files),368)
        self.assertEqual(len(questions),92)

    def test_both_packages_keep_one_note_and_native_card_per_reading(self):
        for language in ('en','fr'):
            _,notes,_,_=inputs(language)
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

    def test_all_sf_pro_labels_still_fit_the_unchanged_pixel_masks(self):
        face=font(ROMAJI_SIZE,roman=True)
        for reading in {c['reading'] for c in self.kana}:
            left,top,right,bottom=face.getbbox(reading)
            self.assertLessEqual(right-left,130,reading)
            self.assertLessEqual(bottom-top,70,reading)

if __name__=='__main__':unittest.main()
