import unittest
from auditor.string_dist import levenshteinDist as lD
#from auditor.cstring_dist import levenshteinDist as clD

class TestStringDist(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lD("",""),0)
        self.assertEqual(lD("astfgl",""),6)
        self.assertEqual(lD("","astfgl"),6)

    def test_equal(self):
        self.assertEqual(lD("astfgl","astfgl"),0)
        self.assertEqual(lD("foobar","foobar"),0)
        
    def test_diff(self):
        self.assertEqual(lD("thought","fought"),2)
        self.assertEqual(lD("cats","mats"),1)
        self.assertEqual(lD("threw","flew"),3)
        
#class TestCStringDist(unittest.TestCase):
#    def test_empty(self):
#        self.assertEqual(clD("",""),0)
#        self.assertEqual(clD("astfgl",""),6)
#        self.assertEqual(clD("","astfgl"),6)
#
#    def test_equal(self):
#        self.assertEqual(clD("astfgl","astfgl"),0)
#        self.assertEqual(clD("foobar","foobar"),0)
#        
#    def test_diff(self):
#        self.assertEqual(clD("thought","fought"),2)
#        self.assertEqual(clD("cats","mats"),1)
#        self.assertEqual(clD("threw","flew"),3)
        
