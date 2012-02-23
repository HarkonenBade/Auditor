from os import path

class FileScanner():
    def __init__(self,queue,tree,pm):
        self.file_queue = queue
        self.data_tree = tree
        self.plugin_manager = pm
    
    def scan(self):
        for f,a in self.file_queue:
            if(a=="attrib_update"):
                attribs = {}
                for p in self.plugin_manager.getPluginIter():
                    attribs.update(p.evaluate_file(path.basename(f),path.dirname(f)))
                if(not self.data_tree.exists(f)):
                    self.data_tree.add(f)
                if(self.data_tree.get(f).attributes != attribs):
                    self.data_tree.update(f,attribs)
                    self.file_queue.add(f,"loc_update")
            elif(a=="loc_update"):
                pass
