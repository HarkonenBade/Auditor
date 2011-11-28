from .event_sanitiser import EventSanitiser
import os

class EventHandler():
    
    def __init__(self,scan_queue,data_tree):
        self.san = EventSanitiser()
        self.san.registerCallback(self.route)
        self.scan_queue = scan_queue
        self.data_tree = data_tree
    
    def process(self,ev):
        self.san.sanitise(ev)
    
    def route(self,ev):
        (evType,evPath,evName) = ev
        fName = os.path.join(evPath,evName)
        if(evType == "IN_DELETE"):
            self.scan_queue.remove(fName)
            self.data_tree.remove(fName)
        else:
            self.scan_queue.add(fName)
