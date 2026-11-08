"""Expand the shared source through the gallery decks' standard interface."""
import hashlib,html,json,uuid
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NS=uuid.UUID('76d92c6f-ceb5-4d12-9dbc-6aa7210f116c')
FIELDS=['Front','Back','Kicker','Meta','Example','Note','RectoVerso search','RectoVerso']
def read(path):return json.loads((ROOT/path).read_text())
def stable_id(text):return int.from_bytes(hashlib.sha256(text.encode()).digest()[:8],'big',signed=True)
def questions():return [q for p in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(p.read_text())]
def ordered(items):
 pending=sorted(items,key=lambda q:(q['stage'],q['priority'],q['id']));result=[];known=set()
 while pending:
  available=next((q for q in pending if set(q.get('requires',[]))<=known),None)
  if available is None:raise ValueError('Missing or cyclic curriculum prerequisites: '+','.join(q['id'] for q in pending[:5]))
  pending.remove(available);result.append(available);known.update(available.get('introduces',[]))
 return result
def inputs(language,artwork=None,only_type=None):
 meta=read('rectoverso.json');words=read(f'source/languages/{language}.json');forms={c['id']:c for c in read('source/kana.json')}
 assets=artwork if artwork is not None else read('artwork/artwork.json')
 guide=read('source/learner-guide.json')
 all_items=ordered(questions());items=[q for q in all_items if only_type is None or q['type']==only_type]
 # Isolated component packages have their own identities; the complete course
 # never replaces a component book or the earlier studied prototype.
 prefix=meta['guidPrefix'] if only_type is None else meta['guidPrefix']+'-preview-'+only_type
 book=str(uuid.uuid5(NS,prefix+'/'+language));deck_id=meta['identityBase']+(100 if language=='fr' else 0)+(0 if only_type is None else 1000+['reading','listening','rule','word','contrast','variant','checkpoint'].index(only_type)*10)
 model_id=meta['identityBase']+10000+(100 if language=='fr' else 0)
 notes=[];media=set();kinds=set()
 for index,q in enumerate(items):
  kind=q['type'];guid=f'{prefix}-{language}-{q["id"]}';payload={'v':1,'book':book,'card':str(uuid.uuid5(NS,guid)),'kind':'occlusion' if kind=='reading' else 'basic','noteID':guid}
  instruction=q['instruction'][language];note=q['note'][language];
  for appendix in q.get('appendices',[]):note+='\n\n'+guide[appendix]['title'][language]+'\n'+guide[appendix].get('noteBody',guide[appendix]['body'])[language]
  back=q.get('answer','');extra='';prompt_audio='';answer_audio=''
  if kind=='reading':
   c=forms[q['target']];f=assets['figures'][q['id']];front='<img src="'+f['question']['file']+'" alt="'+c['kana']+'">';media.add(f['question']['file'])
   payload.update(occlusion=f['occlusion'],preparation=f['preparation'],originalOcclusionAnswer=c['reading'])
   for k in ['source','clean','darkSource','darkClean']:
    media.add(f[k]['file']);extra+='<img src="'+f[k]['file']+'">'
   answer_audio=c['audio'];instruction=words['first']
  elif kind=='listening':
   front=instruction;prompt_audio=q['audio'];back=' / '.join(q['accepted'])+' · '+q['answerReading'];answer_audio=q['audio'];instruction=''
  else:
   front=html.escape(q['display'])
   if kind=='variant':
    f=assets['figures'][q['id']];front='<img src="'+f['dark']['file']+'" alt="'+('Kana in an alternate style' if language=='en' else 'Kana dans un autre style')+'">';media.add(f['dark']['file'])
   answer_audio=q.get('audio','')
   if kind in ['word','checkpoint']:instruction=''  # Context meanings stay after reveal, avoiding cognate reading leaks.
   if kind=='contrast':prompt_audio=q['audio'];back=q['answerKana']+' · '+q['answerReading']
  if prompt_audio:front+='[sound:'+prompt_audio+']';media.add(prompt_audio)
  if answer_audio:back+='[sound:'+answer_audio+']';media.add(answer_audio)
  search={'v':1,'fields':[{'name':'Kana','values':[forms[q['target']]['kana']] if kind=='reading' else q.get('accepted',[q.get('display','')])},{'name':'Exercise' if language=='en' else 'Exercice','values':[kind]}]}
  if q.get('appendices'):search['fields'].append({'name':'Reference' if language=='en' else 'Référence','values':[guide[k]['title'][language] for k in q['appendices']]})
  fields=dict(zip(FIELDS,[front,back,('' if kind in ['reading','rule'] else words.get(kind,q.get('title',{}).get(language,kind))),instruction,q.get('meaning',{}).get(language,''),html.escape(note).replace('\n','<br>'),json.dumps(search,ensure_ascii=False),html.escape(json.dumps(payload,ensure_ascii=False))+extra]))
  notes.append({'guid':guid,'model':'kana','fields':fields,'tags':['exercise::'+kind,'stage::'+str(q['stage'])],'due':index+1,'itemId':q['id']});kinds.add(kind)
 model={'id':model_id,'name':'RectoVerso Kana '+language,'fields':FIELDS,'fieldIDs':{f:stable_id(f'rv-kana/{language}/field/{f}') for f in FIELDS},'templates':[{'name':'Kana practice' if language=='en' else 'Exercices de kana','id':stable_id(f'rv-kana/{language}/template'),'qfmt':'{{Kicker}}<br>{{Front}}<div>{{Meta}}</div>','afmt':'{{FrontSide}}<hr id="answer">{{Back}}<div>{{Example}}</div><div>{{Note}}</div>'}],'css':'.card{font-family:Arial,sans-serif;text-align:center;font-size:28px;background:#FAFAF9;color:#1A1814}img{display:block;max-width:100%;max-height:70vh;margin:auto}.nightMode.card{background:#211E18;color:#EDE6D8}'}
 meta['cards']=len(notes);meta['languages']={k:v|{'cards':len(notes),'sample':f'{prefix}-{k}-{items[0]["id"]}'} for k,v in meta['languages'].items()};meta['guidPrefix']=prefix
 artifact=meta['languages'][language];meta.update(id=artifact['id'],title=artifact['title'],cards=len(notes),sample=notes[0]['guid'],package={'file':f'Japanese-Kana-{language}'+('' if only_type is None else '-'+only_type)+'.apkg'},language=language,component=only_type,bookUUID=book)
 meta['pictures']=sorted(n for n in media if n.endswith('.png'))
 font_by_file={f['file']:f.get('font','NotoSansJP.ttf') for f in assets['files']}
 meta['imageCredits']=[{'file':n,'original':'artwork/fonts/'+font_by_file[n],'source':'Original composition using pinned open fonts','creator':'Simon Pinkas','license':'CC BY 4.0; font OFL-1.1'} for n in meta['pictures']]
 meta['sounds']=sorted(n for n in media if n.endswith('.mp3'))
 return meta,notes,{'kana':model},{'id':deck_id,'name':words['title']+(' · '+words.get(only_type,only_type)+' · '+('review' if language=='en' else 'à relire') if only_type else ''),'description':words['description']}
