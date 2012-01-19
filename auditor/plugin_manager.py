import imp,os

class PluginManager():
    
    def __init__(self,pDir,cDir):
        self.plugins = {}
        self.plugin_dir = pDir
        self.cache_dir = cDir
        self.attributes = {}
    
    def deinit(self):
        for p in self.plugins.values:
            self.unload(p)
    
    def load(self,name):
        (f,p,d) = imp.find_module(name,[self.plugin_dir])
        m = imp.load_module(name,f,p,d)
        f.close()
        
        plugin = self.get_plugin_from_module(m)
        if(plugin != None):
            if(m.__name__ in self.plugins):
                print("ERROR:Conflicting plugin names.")
                return False
            else:
                self.plugins[m.__name__]=(m,plugin)
                attribs = plugin.get_attribute_types()
                for k in attribs:
                    if(k in self.attributes):
                        print("ERROR:Conflicting attribute names.")
                        return False
                    else:
                        self.attributes[k]=attribs[k]
                return True
    
    
    def get_plugin_from_module(self,module):
        for k in module.__dict__:
            if(k.endswith('Plugin')):
                return module.__dict__[k]()
        return None
    
    
    def unload(self,name):
        (m,p) = self.plugins[name]
        attrib_names = p.get_attribute_types().keys()
        
        for a in attrib_names:
            self.attributes.pop(a)
        
        p.unload(self.cache_dir + '/' + m.__name__)
        self.plugins.pop(m.__name__)
    
    def getPluginIter(self):
        return [p for m,p in self.plugins.values()]
    
    def loadAll(self):
        pNames = [x[:-3] for x in os.listdir(self.plugin_dir) if x[-3:] == ".py"]
        for p in pNames:
            self.load(p)
