
class FileScanQueue():
    def __init__(self):
        self.queue = []
        self.first_visit = ""
    
    def add(self,path):
        for (p,f) in self.queue:
            if(p==path):
                self.queue.remove((p,f))
                self.queue.append((p,True))
                return
        self.queue.append((path,False))
    
    def remove(self,path):
        self.queue.remove((path,True))
        self.queue.remove((path,False))
    
    def __next__(self):
        if(len(self.queue)==0):
            raise StopIteration
        (p,f) = self.queue.pop(0)
        if(p == self.first_visit):
            self.queue.append((p,f))
            raise StopIteration
        if(f):
            if(self.first_visit == ""):
                self.first_visit = p
            self.queue.append((p,False))
            return self.__next__()
        return p            
    
    def __iter__(self):
        self.first_visit = ""
        return self
