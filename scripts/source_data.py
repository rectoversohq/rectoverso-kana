"""Expand the shared source through the gallery decks' standard interface."""
import hashlib,html,json,uuid
from pathlib import Path
from introduction_order import check_introduction_order

ROOT=Path(__file__).resolve().parents[1]
NS=uuid.UUID('76d92c6f-ceb5-4d12-9dbc-6aa7210f116c')
FIELDS=['Front','Back','Kicker','Meta','Example','Note','RectoVerso search','RectoVerso','Romaji']
def read(path):return json.loads((ROOT/path).read_text())
def stable_id(text):return int.from_bytes(hashlib.sha256(text.encode()).digest()[:8],'big',signed=True)
def library_id(deck_id):
 """The id RectoVerso gives a deck it reads from an Anki package: its UUID(stableFrom: "anki/deck/<id>"),
 two FNV-1a passes over the text. The payload's `book` is that id, so the gallery, which knows a deck on
 the shelf by it, and the notes agree."""
 text=f'anki/deck/{deck_id}'.encode()
 def fnv(seed):
  value=seed
  for byte in text:value=((value^byte)*0x100000001b3)&0xFFFFFFFFFFFFFFFF
  return value
 return str(uuid.UUID(f'{fnv(0xcbf29ce484222325):016x}{fnv(0x84222325cbf29ce4):016x}'))
def questions():return [q for p in sorted((ROOT/'source/questions').glob('*.json')) for q in json.loads(p.read_text())]
def ordered(items):
 pending=sorted(items,key=lambda q:(q['stage'],q['priority'],q['id']));result=[];known=set()
 while pending:
  available=next((q for q in pending if set(q.get('requires',[]))<=known),None)
  if available is None:raise ValueError('Missing or cyclic curriculum prerequisites: '+','.join(q['id'] for q in pending[:5]))
  pending.remove(available);result.append(available);known.update(available.get('introduces',[]))
 return result
def reading_introductions(items=None):
 # Full authored sequence, including the current reading encounter. Component
 # filtering must not teach future members of that reading's own batch.
 introduced=set();result={}
 for q in ordered(questions() if items is None else items):
  introduced.update(q.get('introduces',[]))
  if q['type']=='reading':result[q['id']]=frozenset(introduced)
 return result
def course(language,artwork=None,only_type=None,beginner_trial=False):
 meta=read('rectoverso.json');words=read(f'source/languages/{language}.json');forms={c['id']:c for c in read('source/kana.json')}
 assets=artwork if artwork is not None else read('artwork/artwork.json')
 guide=read('source/learner-guide.json')
 if beginner_trial and only_type is not None:raise ValueError('Choose a trial or a question-type component, not both')
 all_items=ordered(questions());trial=read('source/beginner-trial.json') if beginner_trial else None
 if trial:
  if trial['items']!=[q['id'] for q in all_items[:20]]:raise ValueError('Trial snapshot no longer matches the reviewed opening')
  items=all_items[:20]
  check_introduction_order(items,forms,assets)
 else:items=[q for q in all_items if only_type is None or q['type']==only_type]
 # Isolated component packages have their own identities; the complete course
 # never replaces a component book or the earlier studied prototype.
 prefix=meta['guidPrefix']+'-beginner-trial' if trial else (meta['guidPrefix'] if only_type is None else meta['guidPrefix']+'-preview-'+only_type)
 deck_id=meta['identityBase']+(100 if language=='fr' else 0)+(2000 if trial else (0 if only_type is None else 1000+['reading','listening','rule','word','contrast','variant','checkpoint'].index(only_type)*10))
 book=library_id(deck_id)
 model_id=meta['identityBase']+(20000 if trial else 10000)+(100 if language=='fr' else 0)
 identity_key=prefix if trial else 'rv-kana'
 notes=[];media=set();kinds=set()
 for index,q in enumerate(items):
  kind=q['type'];guid=f'{prefix}-{language}-{q["id"]}';payload={'v':1,'book':book,'card':str(uuid.uuid5(NS,guid)),'kind':'basic','noteID':guid}
  instruction=q['instruction'][language];hint='';note=q['note'][language];
  # The app's Lesson mode (its Library page, "Prerequisites"): what the card requires and what it
  # introduces, in the course's own tokens. A reading also requires the other kana its figure
  # shows. A type preview alone can't teach what it requires, so it declares nothing.
  if only_type is None:
   requires=list(q.get('requires',[]))
   if kind=='reading':requires+=[k for k in assets['figures'][q['id']]['visibleKana'] if k!=q['target'] and k not in requires]
   if requires:payload['requires']=requires
   if q.get('introduces'):payload['introduces']=list(q['introduces'])
  for appendix in q.get('appendices',[]):
   entry=trial['guide'] if trial and appendix=='course' else guide[appendix]
   note+='\n\n'+entry['title'][language]+'\n'+entry.get('noteBody',entry['body'])[language]
  back=q.get('answer','');extra='';prompt_audio='';answer_audio='';romaji=''
  if kind=='reading':
   c=forms[q['target']];f=assets['figures'][q['id']];front='<img src="'+f['question']['file']+'" alt="'+c['kana']+'">';media.add(f['question']['file'])
   # The answer: the reading, then its row of the chart filling in, a picture beside the answer
   # (the deck kit's card payload, "The words come from the visible fields"), shown once claimed.
   members=[forms[k] for k in sorted(f['visibleKana']+f['ghostKana'],key=lambda k:forms[k]['column'])]
   alt=words['chartDescription'].format(first=members[0]['kana'],row=', '.join(m['kana']+' '+m['reading'] for m in members),taught=len(f['visibleKana']),total=len(members),kana=c['kana'])
   back+='<img src="'+f['answer']['file']+'" alt="'+html.escape(alt,quote=True)+'">';media.add(f['answer']['file'])
   answer_audio=c['audio']
  elif kind=='listening':
   front='';prompt_audio=q['audio'];back=' / '.join(q['accepted']);romaji=q['answerReading'];answer_audio=q['audio'];hint=words['listenOnePrompt'] if len(q['accepted'])>1 else ''
  else:
   front=html.escape(q['display'])
   if kind=='variant':
    f=assets['figures'][q['id']];front='<img src="'+f['dark']['file']+'" alt="'+('Kana in an alternate style' if language=='en' else 'Kana dans un autre style')+'">';media.add(f['dark']['file'])
   answer_audio=q.get('audio','')
   # Context meanings remain on the answer; the task caption supplies no reading clue.
   if kind=='contrast':prompt_audio=q['audio'];back=q['answerKana'];romaji=q['answerReading']
  # Native-payload notes bypass generic Anki template resource extraction.
  if romaji:payload['resources']=[{'name':words['romajiLabel'],'text':romaji}]
  if prompt_audio:front+='[sound:'+prompt_audio+']';media.add(prompt_audio)
  if answer_audio:back+='[sound:'+answer_audio+']';media.add(answer_audio)
  search={'v':1,'fields':[{'name':'Kana','values':[forms[q['target']]['kana']] if kind=='reading' else q.get('accepted',[q.get('display','')])},{'name':'Exercise' if language=='en' else 'Exercice','values':[kind]}]}
  if q.get('appendices'):search['fields'].append({'name':'Reference' if language=='en' else 'Référence','values':[guide[k]['title'][language] for k in q['appendices']]})
  fields=dict(zip(FIELDS,[front,back,instruction,hint,q.get('meaning',{}).get(language,''),html.escape(note).replace('\n','<br>'),json.dumps(search,ensure_ascii=False),html.escape(json.dumps(payload,ensure_ascii=False))+extra,html.escape(romaji)]))
  notes.append({'guid':guid,'model':'kana','fields':fields,'tags':['exercise::'+kind,'stage::'+str(q['stage'])],'due':index+1,'itemId':q['id']});kinds.add(kind)
 details=(
  '{{#Romaji}}<section class="context"><input type="button" class="details-button" value="'
  +html.escape(words['explore'],quote=True)
  +'" onclick="var d=document.getElementById(\'rv-details\');d.hidden=!d.hidden;this.setAttribute(\'aria-expanded\',!d.hidden)" aria-expanded="false" aria-controls="rv-details"><div id="rv-details" hidden><p><strong>'
  +html.escape(words['romajiLabel'])+'</strong><br>{{Romaji}}</p></div></section>{{/Romaji}}'
 )
 model={'id':model_id,'name':'RectoVerso Kana '+('beginner trial ' if trial else '')+language,'fields':FIELDS,'fieldIDs':{f:stable_id(f'{identity_key}/{language}/field/{f}') for f in FIELDS},'templates':[{'name':'Kana practice' if language=='en' else 'Exercices de kana','id':stable_id(f'{identity_key}/{language}/template'),'qfmt':'{{Kicker}}<br>{{Front}}<div>{{Meta}}</div>','afmt':'{{FrontSide}}<hr id="answer">{{Back}}'+details+'<div>{{Example}}</div><div>{{Note}}</div>'}],'css':'.card{font-family:Arial,sans-serif;text-align:center;font-size:28px;background:#FAFAF9;color:#1A1814}img{display:block;max-width:100%;max-height:70vh;margin:auto}.nightMode.card{background:#211E18;color:#EDE6D8}'}
 meta['cards']=len(notes);meta['languages']={k:v|{'cards':len(notes),'sample':f'{prefix}-{k}-{items[0]["id"]}'} for k,v in meta['languages'].items()};meta['guidPrefix']=prefix
 if trial:
  meta['languages']={k:v|{'id':'rectoverso-kana-beginner-trial-'+k,'title':trial['title'][k],'package':{'file':f'Japanese-Kana-{k}-beginner-trial.apkg'}} for k,v in meta['languages'].items()}
 artifact=meta['languages'][language];meta.update(id=artifact['id'],title=artifact['title'],cards=len(notes),sample=notes[0]['guid'],package={'file':f'Japanese-Kana-{language}'+('-beginner-trial' if trial else ('' if only_type is None else '-'+only_type))+'.apkg'},language=language,component='beginner-trial' if trial else only_type,bookUUID=book)
 if trial:meta.update(description=trial['description'][language],headline=trial['headline'])
 meta['pictures']=sorted(n for n in media if n.endswith('.png'))
 font_by_file={f['file']:f.get('font','NotoSansJP.ttf') for f in assets['files']}
 meta['imageCredits']=[{'file':n,'original':'artwork/fonts/'+font_by_file[n],'source':'Original composition using pinned open fonts (OFL-1.1)','creator':'Simon Pinkas','license':'CC-BY-4.0'} for n in meta['pictures']]
 meta['sounds']=sorted(n for n in media if n.endswith('.mp3'))
 return meta,notes,{'kana':model},{'id':deck_id,'name':trial['title'][language] if trial else words['title']+(' · '+words.get(only_type,only_type)+' · '+('review' if language=='en' else 'à relire') if only_type else ''),'description':trial['description'][language] if trial else words['description']}

def declared(language):
 """The complete course as rectoverso.json declares it for one language, in the deck kit's shape
 (kit/docs/getting-started.md): the file without `languages`, plus the language's id, package and
 sample, `deckID` and `language`."""
 meta=read('rectoverso.json');artifact=meta['languages'][language]
 return {k:v for k,v in meta.items() if k!='languages'}|{'id':artifact['id'],'deckID':meta['id'],'language':language,'package':artifact['package'],'sample':artifact['sample']}

def made(language,artwork=None):
 """What the complete course makes of the same facts: rectoverso.json states them, the source decides them.
 The sample isn't among them: it is the owner's choice of one card, which rectoverso.json names."""
 meta,notes,_,_=course(language,artwork)
 return {'cards':len(notes),'pictures':len(meta['pictures']),'imageCredits':meta['imageCredits'],'package':{'file':meta['package']['file']}}

def inputs(language):
 """The deck kit's interface (`python3 kit/check.py`): the declared metadata, the notes, the note
 types and the deck. Refuses a rectoverso.json that states another count, package or credit than the
 course makes, or a sample that isn't one of its cards."""
 expanded=declared(language);facts=made(language);_,notes,models,deck=course(language)
 for key,value in facts.items():
  if expanded[key]!=value:raise ValueError(f'rectoverso.json states another {key} than the course makes: run scripts/metadata.py')
 if expanded['sample'] not in {note['guid'] for note in notes}:raise ValueError(f"rectoverso.json's sample {expanded['sample']} is not a card of the course")
 return expanded,notes,models,deck
