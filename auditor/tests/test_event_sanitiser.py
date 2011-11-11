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

    def test_sucessful(self):
        event = ("Create","/home/tom","foo.py")
        self.evSan.sanitise(event)
        self.assertEqual(self.recorded,"Create:/home/tom/foo.py|")

if __name__ == '__main__':
    unittest.main(verbosity=3)
