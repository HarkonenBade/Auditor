import os,time



class FileDataTree():
    
    class FileNode():
        def __init__(self):
            self.type = "file"
            self.name = ""
            self.attributes = {}
            self.last_scanned = None
    
    class FolderNode():
        def __init__(self):
            self.type = "folder"
            self.name = ""
            self.children = {}
            self.last_scanned = None
    
    def __init__(self):
        self.root = self.FolderNode()
        self.root.last_scanned = time.time()
    
    def add(self,path):
        node = None
        if(os.path.isdir(path)):
            node = self.FolderNode()
        else:
            node = self.FileNode()
        node.name = os.path.basename(path)
        node.last_scanned = time.time()
        pardir = os.path.dirname(path)
        print(node.name+"?"+pardir)
        if(not self.exists(pardir)):
            print("add")
            self.add(pardir)
        parent = self.get(pardir)
        parent.children[node.name] = node

    def get(self,path):
        path_elm = self.shatter_path(path)
        print(path_elm)
        cur = self.root
        if(cur == None):
            return None
        if(path_elm == ['']):
            return cur
        for e in path_elm[1:]:
            if(cur != None and cur.type == "folder" and e in cur.children):
                cur = cur.children[e]
            else:
                return None
        return cur
    
    def remove(self,path):
        if(self.exists(path)):
            parent = self.get(os.path.dirname(path))
            parent.children.pop(os.path.basename(path))
    
    def exists(self,path):
        return (self.get(path) != None)
    
    def shatter_path(self,path):
        (p,n) = os.path.split(path)
        if(n != ''):
            return self.shatter_path(p)+[n]
        return [n]
    
    def update(self,path,data):
        if(self.exists(path)):
            node = self.get(path)
            if(node.type == 'file'):
                node.attributes.update(data)
            else:
                pass
    
    def __iter__(self):
        to_process = []
        for v in self.root.children.items:
            to_process.append(v)
        
        for i in to_process:
            if i.type == 'file':
                yield i
            else:
                for v in i.children.items:
                    to_process.append(v)
