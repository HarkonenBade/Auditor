'''Interface to iNotify system.'''
import os,pyinotify

class INotifyInterface():
    '''FIXME:DOC'''
        
    class EventProcessor(pyinotify.ProcessEvent):
        '''FIXME:DOC'''
        def __init__(self,newOwner):
            '''FIXME:DOC'''
            super().__init__(self)
            self.owner = newOwner
        
        def process_default(self,event):
            '''FIXME:DOC'''
            if(self.owner.handler_list.has_key(event.maskname) and self.owner.handler_list[event.maskname] != None):
                self.owner.handler_list[event.maskname]((event.maskname,event.path,event.name))
    
    
    def __init__(self,tOut):
        '''Initialises the watch manager and notifier. tOut is the largest time that the notifier can hold control for.'''
        self.wm = pyinotify.WatchManager()
        self.mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
        self.notifier = pyinotify.Notifier(self.wm,self.EventProcessor(self),timeout=tOut)
        self.wdd = {}
        self.handler_list = {}

    def deinit(self):
        '''FIXME:DOC'''
        if(self.wdd != None and len(self.wdd)>0):
            self.wm.rm_watch(self.wdd.values())
    
    def startWatch(self,watchDir,recDir=True):
        '''Adds a watch on dir watchDir. If recDir is true then it will recursivly add watches.'''
        self.wdd.update(self.wm.add_watch(watchDir, self.mask, rec=recDir))
    
    def removeWatch(self,watchDir,recDir=True):
        '''Removes the watch on a dir watchDir. If recDir is true it will recursivly remove watches.'''
        removed = self.wm.rm_watch(watchDir,rec=recDir)
        for k,v in removed:
            if(v):#Removed value is set to true if the dir has been removed.
                self.wdd.pop(k)
    
    def registerHandler(self,evType, fn):
        '''Registers a handler fn to handle events of type evType.'''
        self.handler_list[evType] = fn
    
    def removeHandler(self,evType):
        '''Removes the handler for events of evType.'''
        self.handler_list[evType] = None
    
    def setMask(self,mask):
        '''Sets the mask for events received. Should not need to be modified.'''
        self.mask = mask
    
    def scan(self):
        '''Scans the watched directories for changes and reports them via the handling callbacks.'''
        self.notifier.process_events()
        while self.notifier.check_events():  #loop in case more events appear while we are processing
            self.notifier.read_events()
            self.notifier.process_events()
