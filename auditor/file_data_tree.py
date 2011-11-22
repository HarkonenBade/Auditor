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
            self.last_updated = None
    
    def __init__(self):
        self.root = None
    
    def add(self,path):
        node = None
        if(os.path.isdir(path)):
            node = FolderNode()
        else:
            node = FileNode()
        node.name = os.path.basename(path)
        node.last_scanned = time.time()
        pardir = os.path.dirname(path)
        if(not self.exists(pardir)):
            self.add(pardir)
        parent = self.get(pardir)
        parent.children.update({node.name:node})

    def get(self,path):
        path_elm = self.shatter_path(path)
        cur = self.root
        if(cur == None or path_elm[0] != '/'):
            return None
        path_elm.pop()
        for e in path_elm:
            if(cur != None and cur.type == "folder" and cur.children.haskey(e)):
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
    
    
    
