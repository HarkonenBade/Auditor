import event_sanitiser,os

class EventHandler():
    
    def __init__(self,scan_tree):
        self.san = event_sanitiser.EventSanitiser()
        self.san.registerCallback(self.route)
        self.scan_tree = scan_tree
    
    def process(self,ev):
        self.san.sanitise(ev)
    
    def route(self,ev):
        (evType,evPath,evName) = ev
        fName = os.path.join(evPath,evName)
        if(evType == "Delete"):
            self.scan_tree.remove(fName)
        else:
            self.scan_tree.add(fName)
