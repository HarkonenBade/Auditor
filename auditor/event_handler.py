import event_sanitiser,os

class EventHandler():
    
    def __init__(self,scan_queue,data_tree):
        self.san = event_sanitiser.EventSanitiser()
        self.san.registerCallback(self.route)
        self.scan_queue = scan_queue
        self.data_tree = data_tree
    
    def process(self,ev):
        self.san.sanitise(ev)
    
    def route(self,ev):
        (evType,evPath,evName) = ev
        fName = os.path.join(evPath,evName)
        if(evType == "Delete"):
            self.scan_queue.remove(fName)
            self.data_tree.remove(fName)
        else:
            self.scan_queue.add(fName)
