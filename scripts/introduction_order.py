"""Audit actual glyph prerequisites of the basic-kana trial's authored order.

This protects authored content, not the app's runtime queue or learner exposure.
"""

def check_introduction_order(items,forms,artwork):
    known=set()
    for q in items:
        target=None
        if q['type']=='reading':
            target=forms[q['target']]['kana']
            required={forms[key]['kana'] for key in artwork['figures'][q['id']]['visibleKana']}
            required.discard(target)
        else:
            text=''.join(q['accepted']) if q['type']=='listening' else q['display']
            required={c for c in text if '\u3040'<=c<='\u30ff' and c not in '・'}
        missing=required-known
        if missing:raise ValueError('Unintroduced kana in '+q['id']+': '+', '.join(sorted(missing)))
        if target:known.add(target)
