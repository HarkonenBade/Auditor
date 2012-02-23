
class FileScanQueue():
    def __init__(self):
        self.queue = []
        self.first_visit = ""
    
    def add(self,path,action):
        for (p,f,a) in self.queue:
            if(p==path and a==action):
                self.queue.remove((p,f,a))
                self.queue.append((p,True,a))
                return
        self.queue.append((path,False,action))
    
    def remove(self,path):
        for (p,f,a) in self.queue:
            if(p==path):
                self.queue.remove((p,f,a))
    
    def __next__(self):
        if(len(self.queue)==0):
            raise StopIteration
        (p,f,a) = self.queue.pop(0)
        if(p == self.first_visit):
            self.queue.append((p,f,a))
            raise StopIteration
        if(f):
            if(self.first_visit == ""):
                self.first_visit = p
            self.queue.append((p,False,a))
            return self.__next__()
        return (p,a)            
    
    def __iter__(self):
        self.first_visit = ""
        return self
