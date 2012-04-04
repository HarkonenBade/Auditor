import unittest,os
from auditor import inotify_interface

class TestINotifyInterface(unittest.TestCase):
    recorded = ""
    
    def callback(self,ev):
        (t,p,n) = ev
        self.recorded = self.recorded + t + ':' + os.path.join(p,n) + '|'
    
    def setUp(self):
        self.recorded = ""

    def getINotify(self):
        inote = inotify_interface.INotifyInterface(1000)
        inote.setHandler(self.callback)
        return inote
        
    def test_basic(self):
        note = self.getINotify()
        
        note.startWatch("./testbed/")
        f = open("./testbed/foo","w")
        f.write("blar")
        f.close()
        os.remove("./testbed/foo")
        note.scan()
        res =  "IN_CREATE:"+os.getcwd()+"/testbed/foo|"
        res += "IN_MODIFY:"+os.getcwd()+"/testbed/foo|"
        res += "IN_DELETE:"+os.getcwd()+"/testbed/foo|"
        self.assertEqual(self.recorded,res)

if __name__ == '__main__':
    unittest.main(verbosity=3)
