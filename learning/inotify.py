import os
import pyinotify

wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY 

class PTmp(pyinotify.ProcessEvent):
    def process(self,action,event):
        print(action + ": %s" % os.path.join(event.path,event.name))
    
    def process_IN_CREATE(self,event):
        self.process("Create",event)

    def process_IN_DELETE(self,event):
        self.process("Delete",event)

    def process_IN_MODIFY(self,event):
        self.process("Modify",event)

notifier = pyinotify.ThreadedNotifier(wm,PTmp())
notifier.start()
wdd = wm.add_watch('/home/tom/', mask, rec=True)

input("Press enter to end.")

if(wdd['/home/tom/'] > 0):
       wm.rm_watch(wdd.values())

notifier.stop()
