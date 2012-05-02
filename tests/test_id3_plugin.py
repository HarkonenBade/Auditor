import unittest
from os import path
from auditor.plugins.id3_plugin import ID3Plugin

class TestID3Plugin(unittest.TestCase):
    def setUp(self):
        self.id3 = ID3Plugin()
        self.id3.load('')
        
    def test_load(self):
        self.assertEqual(self.id3.name,"ID3 Plugin")
        
    def test_attr(self):
        r = set(self.id3.get_attribute_types().keys())
        self.assertEqual(r,set(['ARTIST','ALBUM','GENRE','YEAR']))
        
    def test_normal(self):
        pass
        
    def test_notid3(self):
        r = self.id3.evaluate_file('test_id3_plugin.py','/home/tom/prj/tests/')
        self.assertEqual(r,{'ARTIST':'',
                            'ALBUM':'',
                            'GENRE':'',
                            'YEAR':0})
                            
    def test_notthere(self):
        r = self.id3.evaluate_file('fakefile','/home/tom/')
        self.assertEqual(r,{'ARTIST':'',
                            'ALBUM':'',
                            'GENRE':'',
                            'YEAR':0})
                            
    
    def test_mangledyear(self):
        pass
        

