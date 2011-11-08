'''FIXME:DOC'''
import os


class EventSanitiser():
    '''FIXME:DOC'''
    callback = None
    blocked_paths = []
    
    def init(self):
        '''FIXME:DOC'''
        pass
    
    def deinit(self):
        '''FIXMEDOC'''
        pass
    
    def addBlockedPath(self,path):
        '''FIXME:DOC'''
        pass
    
    def rmBlockedPath(self,path):
        '''FIXME:DOC'''
        pass
    
    def registerCallback(self,fn):
        '''FIXME:DOC'''
        pass
    
    def sanitise(self,ev):
        '''Sanitises events passed to it. Removes events in blocked paths and on paths containing a . or for files beginning with .'''
        (evType,evPath,evName) = ev
        
        for p in self.blocked_paths:
            if(evPath.startsWith(p)):
                return
        
        if(evPath.contains('.')):
            return
        
        if(evName.startsWith('.')):
            return
        
        callback(ev)

