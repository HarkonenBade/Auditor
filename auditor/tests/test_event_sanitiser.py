import unittest
from auditor import event_sanitiser

class TestEventSanitiser(unittest.TestCase):
    recorded = ""
    
    def callback(self,ev):
        (t,p,n) = ev
        self.recorded = self.recorded + t + ':' + p + '/' + n + '|'
    
    def setUp(self):
        self.recorded = ""

    def getEvSan(self):
        evSan = event_sanitiser.EventSanitiser()
        evSan.registerCallback(self.callback)
        return evSan
        
    def test_basic_sanitise(self):
        evSan = self.getEvSan()
        
        event = ("Create","/home/tom","foo.py")
        evSan.sanitise(event)
        self.assertEqual(self.recorded,"Create:/home/tom/foo.py|")
    
    def test_blocked_path_addition(self):
        evSan = self.getEvSan()
        
        path = "/home/tom"
        events = [("Create","/media/RAID","blar.gif"),("Delete","/home/tom/doc/test","thing.pdf"),("Modify","/media/RAID","heim.frg")]
        
        evSan.addBlockedPath(path)
        
        for e in events:
            evSan.sanitise(e)
        
        self.assertEqual(self.recorded,"Create:/media/RAID/blar.gif|Modify:/media/RAID/heim.frg|")
        
    def test_blocked_path_removal(self):
        evSan = self.getEvSan()
        
        paths=["/home/tom","/media/RAID"]
        events = [("Create","/media/RAID","blar.gif"),("Delete","/home/tom/doc/test","thing.pdf"),("Modify","/media/RAID","heim.frg")]
        
        for p in paths:
            evSan.addBlockedPath(p)
        
        evSan.rmBlockedPath("/home/tom")
        
        for e in events:
            evSan.sanitise(e)
        
        self.assertEqual(self.recorded,"Delete:/home/tom/doc/test/thing.pdf|")


if __name__ == '__main__':
    unittest.main(verbosity=3)
