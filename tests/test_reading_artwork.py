"""Reading cards: the big kana as the question, its row of the chart lit behind the review."""
import html
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import square,span,row,W,H,CELL,MARGIN
from source_data import course,questions,ordered,reading_introductions

ROLES=('source','clean','darkSource','darkClean')

class ReadingArtworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kana=json.loads((ROOT/'source/kana.json').read_text())
        cls.introductions=reading_introductions()
        cls.figures=json.loads((ROOT/'artwork/artwork.json').read_text())['figures']

    def test_the_figure_is_a_rows_width_and_taller_than_any_window(self):
        self.assertEqual((W,H),(2040,4760))
        self.assertGreater(H/W,874/402)
        for c in self.kana:
            x,y,w,h=square(c)
            self.assertEqual((x,w,h),(MARGIN+CELL*c['column'],CELL,CELL))
        # や/ゆ/よ and わ/を in their standard slots, ん alone.
        self.assertEqual({(c['row'],c['column']) for c in self.kana if c['row'] in (7,9,10) and c['script']=='hira'},{(7,0),(7,2),(7,4),(9,0),(9,4),(10,0)})

    def test_all_92_figures_are_lit_rows_with_one_titled_region(self):
        for target in self.kana:
            forms=[c for c in self.kana if c['script']==target['script']]
            figure=self.figures['read-'+target['id']]
            taught,ghosts=row(target,forms,self.introductions['read-'+target['id']])
            members=sorted(taught+ghosts,key=lambda c:c['column'])
            def box():
                x,y,w,h=span(members);return [[x/W,y/H],[w/W,h/H]]
            with self.subTest(target=target['id']):
                self.assertEqual({c['row'] for c in members},{target['row']})
                self.assertEqual(len(members),sum(c['row']==target['row'] for c in forms))
                self.assertIn(target,taught)
                # The region is the whole row, so the app keeps all of it in the window.
                x,y,w,h=span(members)
                self.assertEqual((x,w),(MARGIN+CELL*members[0]['column'],CELL*(members[-1]['column']-members[0]['column']+1)))
                self.assertEqual(figure['visibleKana'],[c['id'] for c in taught])
                self.assertEqual(figure['ghostKana'],[c['id'] for c in ghosts])
                occlusion=figure['occlusion'];preparation=figure['preparation']
                self.assertEqual(occlusion['imageSize'],[W,H])
                self.assertEqual(occlusion['ordinal'],forms.index(target)+1)
                self.assertEqual(occlusion['box'],box())
                self.assertEqual((occlusion['label'],occlusion['mode'],occlusion['siblings']),(target['reading'],'hideAll',[]))
                self.assertEqual(preparation['mode'],'lit')
                self.assertEqual(preparation['regions'],[{'id':target['id'],'ordinal':forms.index(target)+1,'kind':'label','geometry':{'kind':'rect','coordinates':sum(box(),[])},'answer':target['reading'],'title':target['reading']}])
                self.assertEqual(occlusion['imageName'],figure['source']['file'])
                for role in ROLES:self.assertEqual(preparation[role],figure[role])

    def test_row_names_avoid_collisions_with_every_previous_table_edition(self):
        files=set()
        for target in self.kana:
            f=self.figures['read-'+target['id']]
            for role in ROLES:
                asset=f[role];files.add(asset['file'])
                self.assertEqual((asset['width'],asset['height']),(W,H))
                self.assertTrue(asset['file'].startswith('rv-kana-'+target['id']+'-litrow-'))
            self.assertEqual(f['question']['file'],'rv-kana-'+target['id']+'-question.png')
        self.assertEqual(len(files),368)

    def test_both_packages_keep_one_note_and_card_per_reading(self):
        for language in ('en','fr'):
            _,notes,_,_=course(language)
            reading=[n for n in notes if n['itemId'].startswith('read-')]
            self.assertEqual(len(reading),92)
            payloads=[json.JSONDecoder().raw_decode(html.unescape(n['fields']['RectoVerso']))[0] for n in reading]
            self.assertEqual(len({p['card'] for p in payloads}),92)
            for n,p in zip(reading,payloads):
                self.assertEqual(p['kind'],'occlusion')
                self.assertEqual(p['noteID'],n['guid'])
                self.assertEqual(p['occlusion'],self.figures[n['itemId']]['occlusion'])
                self.assertEqual(n['fields']['Front'],'<img src="'+self.figures[n['itemId']]['question']['file']+'" alt="'+next(k['kana'] for k in self.kana if 'read-'+k['id']==n['itemId'])+'">')
            self.assertEqual([n['due'] for n in notes],list(range(1,len(notes)+1)))

if __name__=='__main__':unittest.main()
