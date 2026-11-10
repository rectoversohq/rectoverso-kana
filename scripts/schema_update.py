"""Verify an update's existing schema identities and approved trailing fields."""

def check_schema_update(before,after,expected):
    if set(before)!=set(after) or set(after)!=set(expected):
        raise ValueError('Update changed model identity')
    for mid,old in before.items():
        current=after[mid];wanted=expected[mid]
        if current!=wanted:
            raise ValueError('Updated schema differs from current package')
        old_fields,old_templates=old
        fields,templates=current
        if fields[:len(old_fields)]!=old_fields or templates!=old_templates:
            raise ValueError('Update changed existing field or template identity')
        appended=fields[len(old_fields):]
        if appended and ([name for name,_ in appended]!=['Romaji'] or len(fields)!=9):
            raise ValueError('Update appended an unapproved field')
