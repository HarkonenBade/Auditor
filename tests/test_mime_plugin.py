import unittest
from auditor.plugins.mime_plugin import mimePlugin

class TestmimePlugin(unittest.TestCase):
    def test_load(self):
        p = mimePlugin()
        p.load('')
        self.assertEqual(p.name,"mime Plugin")
    
    def test_eval(self):
        p = mimePlugin()
        p.load('')
        at = p.evaluate_file("test_mime_plugin.py","/home/tom/prj/tests/")
        self.assertEquals(at,{'MIME':'text/x-python'})
    
    def test_attr_types(self):
        p = mimePlugin()
        p.load('')
        t = list(p.get_attribute_types().keys())
        self.assertEqual(t,['MIME'])
        
    def test_eval_miss(self):
        p = mimePlugin()
        p.load('')
        at = p.evaluate_file("fake_file","/home/tom/")
        self.assertEqual(at,{'MIME':''})
