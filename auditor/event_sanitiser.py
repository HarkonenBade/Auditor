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
        self.blocked_paths.append(path)
    
    def rmBlockedPath(self,path):
        '''FIXME:DOC'''
        self.blocked_path.remove(path)
    
    def registerCallback(self,fn):
        '''FIXME:DOC'''
        self.callback = fn
    
    def sanitise(self,ev):
        '''Sanitises events passed to it. Removes events in blocked paths and on paths containing a . or for files beginning with .'''
        (evType,evPath,evName) = ev
        
        for p in self.blocked_paths:
            if(evPath.startswith(p)):
                print("Stripped due to blocked path")
                return
        
        if(evPath.find('.') >= 0):
            print("Stripped due to . in path")
            return
        
        if(evName.startswith('.')):
            print("Stripped due to start .")
            return
        
        self.callback(ev)

