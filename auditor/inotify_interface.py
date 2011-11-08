'''FIXME:DOC'''
import os,pyinotify

class INotifyInterface():
    '''FIXME:DOC'''
    wm = None 
    notifier = None
    wmm = None
    mask = None
    handler_list = {}
    
    class EventProcessor(pyinotify.ProcessEvent):
        '''FIXME:DOC'''
        def process_default(self,event):
            '''FIXME:DOC'''
            if(inotify_interface.handler_list.has_key(event.maskname)):
                inotify_interface.handler_list[event.maskname]((event.maskname,event.path,event.name))
    
    
    def init(self,tOut):
        '''FIXME:DOC'''
        self.wm = pyinotify.WatchManager()
        self.mask = pyinotify.IN_CREATE | pyinotify.INDELETE | pyinotify.IN_MODIFY
        self.notifier = pyinotify.Notifier(wm,self.EventProcessor(),timeout=tOut)
    
    def deinit(self):
        '''FIXME:DOC'''
        pass
    
    def startWatch(self,dir):
        '''FIXME:DOC'''
        pass
    
    def removeWatch(self,dir):
        '''FIXME:DOC'''
        pass
    
    def registerHandler(self,evType, fn):
        '''FIXME:DOC'''
        pass
    
    def removeHandler(self,evType):
        '''FIXME:DOC'''
        pass
    
    def setMask(self,mask):
        '''FIXME:DOC'''
        pass
