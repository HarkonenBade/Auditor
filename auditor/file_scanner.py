from os import path

class FileScanner():
    def __init__(self,queue,tree,pm):
        self.file_queue = queue
        self.data_tree = tree
        self.plugin_manager = pm
    
    def scan(self):
        for f in self.file_queue:
            attribs = {}
            for p in self.plugin_manager.getPluginIter():
                attribs.update(p.evaluate_file(path.basename(f),path.dirname(f)))
            if(not self.data_tree.exists(f)):
                self.data_tree.add(f)
            self.data_tree.update(f,attribs)
