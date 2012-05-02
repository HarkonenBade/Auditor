import unittest,os
from auditor import file_data_tree

class TestFileDataTree(unittest.TestCase):
    
    def test_creation(self):
        f = file_data_tree.FileDataTree()
        self.assertEqual(f.exists("/"),True)
        
    def test_addition(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        self.assertEqual(f.exists('/home/tom/prj/tests/test_file_data_tree.py'),True)
        
    def test_get(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        g = f.get('/home/tom/prj/tests/test_file_data_tree.py')
        self.assertEqual(g.name,"test_file_data_tree.py")
        
    def test_remove(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        self.assertEqual(f.exists('/home/tom/prj/tests/test_file_data_tree.py'),True)
        f.remove('/home/tom/prj/tests/test_file_data_tree.py')
        self.assertEqual(f.exists('/home/tom/prj/tests/test_file_data_tree.py'),False)
        self.assertEqual(f.exists('/home/tom/prj/tests/'),True)
        
    def test_update(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        g = f.get('/home/tom/prj/tests/test_file_data_tree.py')
        self.assertEqual(g.attributes,{})
        f.update('/home/tom/prj/tests/test_file_data_tree.py',{'TAG':42})
        g = f.get('/home/tom/prj/tests/test_file_data_tree.py')
        self.assertEqual(g.attributes,{'TAG':42})
        
    def test_save_load(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        f.save('/tmp/foo.tr')
        g = file_data_tree.FileDataTree()
        g.load('/tmp/foo.tr')
        self.assertEqual(g.exists('/home/tom/prj/tests/test_file_data_tree.py'),True)
        
    def test_save_load_nc(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        f.save('/tmp/foo.tr',False)
        g = file_data_tree.FileDataTree()
        g.load('/tmp/foo.tr',False)
        self.assertEqual(g.exists('/home/tom/prj/tests/test_file_data_tree.py'),True)
    
    def test_iter(self):
        f = file_data_tree.FileDataTree()
        f.add('/home/tom/prj/tests/test_file_data_tree.py')
        f.add('/home/tom/prj/tests/test_string_enc.py')
        f.add('/home/tom/prj/tests/test_event_sanitiser.py')
        t = set()
        for (p,n) in f:
            t.add(n.name)
        self.assertEqual(t,set(["test_file_data_tree.py","test_string_enc.py","test_event_sanitiser.py"]))
        t = set()
        for (p,n) in f.folder_iter():
            t.add(n.name)
        self.assertEqual(t,set(["home","tom","prj","tests"]))
        
