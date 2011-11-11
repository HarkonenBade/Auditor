import unittest
from auditor import event_sanitiser

class TestEventSanitiser(unittest.TestCase):
    recorded = ""
    evSan = None
    
    def callback(self,ev):
        (t,p,n) = ev
        self.recorded = self.recorded + t + ':' + p + '/' + n + '|'
    
    def setUp(self):
        self.recorded = ""
        self.evSan = event_sanitiser.EventSanitiser()
        self.evSan.registerCallback(self.callback)

    def test_basic_sanitise(self):
        event = ("Create","/home/tom","foo.py")
        self.evSan.sanitise(event)
        self.assertEqual(self.recorded,"Create:/home/tom/foo.py|")
    
    def test_blocked_path_addition(self):
        path = "/home/tom"
        events = [("Create","/media/RAID","blar.gif"),("Delete","/home/tom/doc/test","thing.pdf"),("Modify","/media/RAID","heim.frg")]
        
        self.evSan.addBlockedPath(path)
        
        for e in events:
            self.evSan.sanitise(e)
        
        self.assertEqual(self.recorded,"Create:/media/RAID/blar.gif|Modify:/media/RAID/heim.frg|")
    

if __name__ == '__main__':
    unittest.main(verbosity=3)
