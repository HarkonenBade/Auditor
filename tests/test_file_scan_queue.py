import unittest,os
from auditor.file_scan_queue import FileScanQueue

class TestFileScanQueue(unittest.TestCase):
    
    def test_create(self):
        f = FileScanQueue()
        self.assertEqual(f.queue,[])
    
    def test_add(self):
        f = FileScanQueue()
        self.assertEqual(f.queue,[])
        f.add("foo","t")
        self.assertEqual(f.queue,[('foo',False,'t')])
        f.add("bar","t")
        self.assertEqual(f.queue,[('foo',False,'t'),('bar',False,'t')])
        f.add("foo","t")
        self.assertEqual(f.queue,[('bar',False,'t'),('foo',True,'t')])
        
    def test_remove(self):
        f = FileScanQueue()
        f.add("foo","t")
        f.add("bar","t")
        self.assertEqual(f.queue,[('foo',False,'t'),('bar',False,'t')])
        f.remove("foo")
        self.assertEqual(f.queue,[('bar',False,'t')])
        f.remove("bar")
        self.assertEqual(f.queue,[])
    
    def test_iter(self):
        f = FileScanQueue()
        f.add("foo","t")
        f.add("bar","t")
        f.add("foo","t")
        self.assertEqual(f.queue,[('bar',False,'t'),('foo',True,'t')])
        t = []
        for k in f:
            t += [k]
        self.assertEqual(t,[("bar",'t')])
        self.assertEqual(f.queue,[('foo',False,'t')])
        t = []
        for k in f:
            t += [k]
        self.assertEqual(t,[("foo",'t')])
        self.assertEqual(f.queue,[])
