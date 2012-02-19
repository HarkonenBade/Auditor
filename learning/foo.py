import pyinotify


class EventProcessor(pyinotify.ProcessEvent):
    '''FIXME:DOC'''
    def __init__(self,newH):
        '''FIXME:DOC'''
        super(EventProcessor,self).__init__()
        self.handler_list = newH
    
    def process_default(self,event):
        '''FIXME:DOC'''
        if(event.maskname in self.handler_list and self.handler_list[event.maskname] != None):
            print(event.maskname)#self.handler_list[event.maskname]((event.maskname,event.path,event.name))

handler_list = {}
wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
notifier = pyinotify.Notifier(wm,EventProcessor(handler_list),timeout=100)
wdd = {}


def blar(ev):
    (t,p,n) = ev
    print(t+":"+p+"/"+n)

handler_list["Create"] = blar
handler_list["Delete"] = blar
handler_list["Modify"] = blar

wdd.update(wm.add_watch("/home/tom/ni/", mask, rec=True))

flar = ""

while flar != "e":
    notifier.process_events()
    while notifier.check_events():  #loop in case more events appear while we are processing
        notifier.read_events()
        notifier.process_events()
    flar = input("Ni")
