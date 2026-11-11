"""Reading and alternate-form cards: one kana alone in its writing square, lit; a reading's row after the answer."""
import html
import json
import sys
import unittest
from pathlib import Path
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from render_artwork import font,FACES,MARGIN,SIDE,SLOT,SQUARE,STRIP_H,STRIP_PAD,STRIP_W,W,H,ink,ink_box,normalized_square,page,row,strip,strip_slot,PALETTES,STRIP,hexrgb
from source_data import course,questions,reading_introductions

ROLES=('source','clean','darkSource','darkClean')

class ReadingArtworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kana=json.loads((ROOT/'source/kana.json').read_text())
        cls.introductions=reading_introductions()
        cls.figures=json.loads((ROOT/'artwork/artwork.json').read_text())['figures']
        cls.variants=[q for q in questions() if q['type']=='variant']

    def test_the_page_opens_with_the_square_sized_by_the_windows_height(self):
        # The app opens a lit figure at max(canvas width / figure width, window height / figure
        # height) when that beats its 44-point rule, and decodes a figure at 4,096 pixels at most.
        self.assertLessEqual(max(W,H),4096)
        self.assertEqual(SQUARE,((W-SIDE)//2,(H-SIDE)//2,SIDE,SIDE))
        self.assertEqual(SIDE*2,H)
        # The window's height sets the scale wherever the page is wider for its height than the
        # canvas is for the window: a 402-point iPhone (a window about 572 points high), a 430-point
        # one (about 634) and the closed Duo (466 points wide, about 436 high).
        for canvas,window in ((402,572),(430,634),(466,436)):
            self.assertGreater(window/H,canvas/W)
            self.assertGreaterEqual(SIDE*window/H,44)
        # In book pose the canvas, 951 points wide, sets it: the square stays inside a page's
        # window, 415 points wide, and keeps three pixels a point.
        self.assertLessEqual(SIDE*951/W,415)
        self.assertGreaterEqual(W/951,3)
        self.assertEqual(normalized_square(),[[SQUARE[0]/W,SQUARE[1]/H],[SIDE/W,SIDE/H]])

    def test_every_kana_is_centred_in_its_square_and_keeps_to_it(self):
        drawn=[(c['kana'],'sans') for c in self.kana]+[(q['display'],q['fontStyle']) for q in self.variants]
        self.assertEqual({face for _,face in drawn},set(FACES))
        for kana,face in drawn:
            with self.subTest(kana=kana,face=face):
                x,y,w,h=ink_box(kana,face)
                self.assertEqual(ink(kana,face).size,(w,h))
                self.assertLessEqual(abs((x+w/2)-W/2),0.5)
                self.assertLessEqual(abs((y+h/2)-H/2),0.5)
                self.assertGreaterEqual(x-SQUARE[0],MARGIN)
                self.assertGreaterEqual(y-SQUARE[1],MARGIN)
        # Each face's size makes あ's ink 73.5 % of the square: about half a phone's width.
        for name,size in FACES.values():
            probe=Image.new('L',(3*size,3*size),0);ImageDraw.Draw(probe).text((size,size),'あ',font=font(size,name),fill=255)
            box=probe.getbbox();self.assertLessEqual(abs(box[2]-box[0]-0.735*SIDE),2,name)

    def test_a_page_is_its_paper_the_squares_cross_and_the_kana_alone(self):
        for mode,pal in PALETTES.items():
            paper,ghost,ink_color=(hexrgb(pal[k]) for k in ('paper','ghost','ink'))
            clean=page(None,None,pal).convert('RGB');source=page('し','sans',pal).convert('RGB')
            self.assertEqual({c for _,c in clean.getcolors()},{paper,ghost})
            self.assertIn(ink_color,{c for _,c in source.getcolors(1<<24)})
            # Nothing is drawn outside the square, and the cross runs through its middle.
            x,y,_,_=SQUARE
            for image in (clean,source):
                outside=image.copy();outside.paste(paper,(x,y,x+SIDE,y+SIDE))
                self.assertEqual(outside.getextrema(),tuple((v,v) for v in paper))
            self.assertEqual(clean.getpixel((W//2,y+2)),ghost)
            self.assertEqual(clean.getpixel((x+2,H//2)),ghost)
            self.assertEqual(clean.getpixel((x+2,y+2)),paper)

    def test_all_92_readings_are_lit_squares_with_one_titled_region(self):
        for target in self.kana:
            forms=[c for c in self.kana if c['script']==target['script']]
            figure=self.figures['read-'+target['id']]
            taught,ghosts=row(target,forms,self.introductions['read-'+target['id']])
            with self.subTest(target=target['id']):
                self.assertEqual({c['row'] for c in taught+ghosts},{target['row']})
                self.assertEqual(len(taught+ghosts),sum(c['row']==target['row'] for c in forms))
                self.assertIn(target,taught)
                self.assertEqual(figure['visibleKana'],[c['id'] for c in taught])
                self.assertEqual(figure['ghostKana'],[c['id'] for c in ghosts])
                self.check_lit(figure,target['id'],target['reading'],forms.index(target)+1,target['id'])
                self.assertEqual(figure['row']['file'],'rv-kana-'+target['id']+'-rowstrip.png')
                self.assertEqual((figure['row']['width'],figure['row']['height']),(STRIP_W,STRIP_H))

    def test_the_eight_alternate_forms_are_lit_squares_in_their_own_face(self):
        self.assertEqual([q['fontStyle'] for q in self.variants],['textbook']*4+['serif']*4)
        self.assertEqual(''.join(q['display'] for q in self.variants),'さきりふそシツン')
        files={f['file']:f for f in json.loads((ROOT/'artwork/artwork.json').read_text())['files']}
        for q in self.variants:
            with self.subTest(variant=q['id']):
                figure=self.figures[q['id']]
                self.check_lit(figure,q['id'],q['answer'],1,q['id'])
                self.assertNotIn('row',figure)
                for role in ('source','darkSource','question'):
                    self.assertEqual(files[figure[role]['file']]['font'],FACES[q['fontStyle']][0])
        for language,style in (('en','textbook-style'),('fr','style scolaire')):
            for q in self.variants[:4]:
                self.assertIn('Klee One',q['note'][language]);self.assertIn(style,q['note'][language])
                self.assertNotIn('Yomogi',q['note'][language])

    def check_lit(self,figure,region_id,reading,ordinal,key):
        occlusion=figure['occlusion'];preparation=figure['preparation']
        self.assertEqual(occlusion['imageSize'],[W,H])
        self.assertEqual(occlusion['ordinal'],ordinal)
        self.assertEqual(occlusion['box'],normalized_square())
        self.assertEqual((occlusion['label'],occlusion['mode'],occlusion['siblings']),(reading,'hideAll',[]))
        self.assertEqual(preparation['mode'],'lit')
        self.assertEqual(preparation['regions'],[{'id':region_id,'ordinal':ordinal,'kind':'label','geometry':{'kind':'rect','coordinates':sum(normalized_square(),[])},'answer':reading,'title':reading}])
        self.assertEqual(occlusion['imageName'],figure['source']['file'])
        for role in ROLES:
            self.assertEqual(preparation[role],figure[role])
            self.assertEqual((figure[role]['width'],figure[role]['height']),(W,H))
        # New names keep an update from colliding with any earlier edition's pictures; the square
        # without a kana is one picture, shared by every figure.
        self.assertEqual(figure['source']['file'],f'rv-kana-{key}-square-light-source.png')
        self.assertEqual(figure['darkSource']['file'],f'rv-kana-{key}-square-dark-source.png')
        self.assertEqual((figure['clean']['file'],figure['darkClean']['file']),('rv-kana-square-light-clean.png','rv-kana-square-dark-clean.png'))
        self.assertEqual(figure['question']['file'],f'rv-kana-{key}-question.png')

    def test_the_rows_strip_puts_each_kana_in_its_role_and_slot(self):
        paper,cream,faint,gold=(hexrgb(STRIP[k]) for k in ('paper','ink','ghost','accent'))
        hira=[c for c in self.kana if c['script']=='hira']
        def colors(image,c,members):
            x=strip_slot(c,members);return {k for _,k in image.crop((x-SLOT//2,0,x+SLOT//2,STRIP_H)).getcolors(1<<24)}
        # し, once さ is taught: さ in cream, し in gold, す せ そ faint.
        shi=next(c for c in hira if c['kana']=='し');members=[c for c in hira if c['row']==shi['row']]
        image=strip(shi,members[:2],members[2:]).convert('RGB')
        self.assertEqual(image.size,(STRIP_W,STRIP_H))
        self.assertEqual(image.getpixel((0,0)),paper)
        for c,(present,absent) in zip(members,[((cream,),(gold,faint)),((gold,),(cream,faint))]+[((faint,),(cream,gold))]*3):
            found=colors(image,c,members)
            for color in present:self.assertIn(color,found,c['kana'])
            for color in absent:self.assertNotIn(color,found,c['kana'])
        self.assertEqual([strip_slot(c,members) for c in members],[STRIP_PAD+SLOT*i+SLOT//2 for i in range(5)])
        # や ゆ よ keep their vowels' slots; ん, a row of one, sits in the middle.
        ya=[c for c in hira if c['row']==7];self.assertEqual([strip_slot(c,ya) for c in ya],[STRIP_PAD+SLOT*i+SLOT//2 for i in (0,2,4)])
        n=[c for c in hira if c['row']==10];self.assertEqual([strip_slot(c,n) for c in n],[STRIP_W//2])

    def test_one_clean_pair_and_new_names_for_every_picture(self):
        files=set()
        for key,figure in self.figures.items():
            if not (key.startswith('read-') or key.startswith('variant-')):continue
            files.update(figure[role]['file'] for role in ROLES)
            if 'row' in figure:files.add(figure['row']['file'])
        self.assertEqual(len(files),2*(92+8)+2+92)
        for name in files:self.assertTrue('-square-' in name or name.endswith('-rowstrip.png'),name)

    def test_both_packages_keep_one_note_and_card_per_reading_and_alternate_form(self):
        for language,label in (('en','Row'),('fr','Ligne')):
            _,notes,_,_=course(language)
            lit=[n for n in notes if n['itemId'].startswith(('read-','variant-'))]
            self.assertEqual(len(lit),100)
            payloads=[json.JSONDecoder().raw_decode(html.unescape(n['fields']['RectoVerso']))[0] for n in lit]
            self.assertEqual(len({p['card'] for p in payloads}),100)
            for n,p in zip(lit,payloads):
                figure=self.figures[n['itemId']]
                self.assertEqual(p['kind'],'occlusion')
                self.assertEqual(p['noteID'],n['guid'])
                self.assertEqual(p['occlusion'],figure['occlusion'])
                self.assertEqual(p['preparation'],figure['preparation'])
                self.assertIn('src="'+figure['question']['file']+'"',n['fields']['Front'])
                # Anki packs what only the app shows: each page, and a reading's strip.
                for role in ROLES:self.assertIn('<img src="'+figure[role]['file']+'">',n['fields']['RectoVerso'])
                if n['itemId'].startswith('read-'):
                    target=next(k for k in self.kana if 'read-'+k['id']==n['itemId'])
                    self.assertEqual(n['fields']['Front'],'<img src="'+figure['question']['file']+'" alt="'+target['kana']+'">')
                    self.assertEqual(p['resources'],[{'name':label,'text':'','images':[figure['row']['file']]}])
                    self.assertIn('<img src="'+figure['row']['file']+'">',n['fields']['RectoVerso'])
                    # The row is the strip's alone: the note no longer opens with it as text.
                    self.assertNotIn(' · ',n['fields']['Note'])
                    self.assertNotIn(target['kana']+' '+target['reading'],n['fields']['Note'])
                else:self.assertNotIn('resources',p)
            self.assertEqual([n['due'] for n in notes],list(range(1,len(notes)+1)))

if __name__=='__main__':unittest.main()
