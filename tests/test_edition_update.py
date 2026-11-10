"""Existing identities/history must survive an edition with new questions."""
import importlib.util
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
spec=importlib.util.spec_from_file_location('edition_update',ROOT/'scripts/checks/validate-update.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
check=module.check_identity_update

class EditionUpdateTests(unittest.TestCase):
 def test_allows_new_questions_and_preserves_studied_cards(self):
  self.assertEqual(check({'old','new'},{'old':10},{'old':10,'new':20},[(100,10,'studied')],[(100,10,'studied'),(200,20,'new')]),['new'])
 def test_rejects_removed_old_question_changed_ids_or_history_and_wrong_inventory(self):
  cases=[
   ({'new'},{'new':20},[(200,20,'new')]),
   ({'old','new'},{'old':11,'new':20},[(100,11,'studied'),(200,20,'new')]),
   ({'old','new'},{'old':10,'new':20},[(101,10,'studied'),(200,20,'new')]),
   ({'old','new'},{'old':10,'new':20},[(100,10,'new'),(200,20,'new')]),
   ({'old','new'},{'old':10},[(100,10,'studied')]),
   ({'old','new'},{'old':10,'new':20},[(100,10,'studied')]),
   ({'old','new'},{'old':10,'new':20},[(100,10,'studied'),(200,10,'new')]),
  ]
  for expected,notes,cards in cases:
   with self.subTest(expected=expected,notes=notes,cards=cards),self.assertRaises(ValueError):
    check(expected,{'old':10},notes,[(100,10,'studied')],cards)

if __name__=='__main__':unittest.main()
