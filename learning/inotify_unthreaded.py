import os
import pyinotify

wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY 

class PTmp(pyinotify.ProcessEvent):
    def process(self,action,event):
        if(event.path.find('.') == -1 and not event.name.startswith('.')):
            print(action + ": %s" % os.path.join(event.path,event.name))
    
    def process_IN_CREATE(self,event):
        self.process("Create",event)

    def process_IN_DELETE(self,event):
        self.process("Delete",event)

    def process_IN_MODIFY(self,event):
        self.process("Modify",event)

notifier = pyinotify.Notifier(wm,PTmp(),timeout=1000)

wdd = wm.add_watch('/home/tom/', mask, rec=True)


def quick_check(notifier):
          assert notifier._timeout is not None, 'Notifier must be constructed with a short timeout.'
          notifier.process_events()
          while notifier.check_events():  #loop in case more events appear while we are processing
                notifier.read_events()
                notifier.process_events()


while input("Press e to exit. Otherwise a re-scan will occur.") != 'e':
	quick_check(notifier)

if(wdd['/home/tom/'] > 0):
	wm.rm_watch(wdd['/home/tom/'], rec=True)

