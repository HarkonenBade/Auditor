import imp,os,inspect

class PluginManager():
    
    def __init__(self):
        self.plugins = {}
        self.plugin_dir = ""
        self.cache_dir = ""
        self.attributes = {}
    
    def deinit(self):
        for p in self.plugins.values:
            self.unload(p)
    
    def load(self,name):
        (f,p,d) = imp.find_module(name,[os.path.join(self.plugin_dir,name)])
        m = imp.load_module(name,f,p,d)
        f.close()
        
        plugin = self.get_plugin_from_module(m)
        if(plugin != None):
            if(self.plugins.haskey(m.__name__)):
                print("ERROR:Conflicting plugin names.")
                return False
            else:
                self.plugins.update(m.__name__,(m,plugin))
                attribs = plugin.get_attribute_types()
                for (k,v) in attribs:
                    if(self.attributes.haskey(k)):
                        print("ERROR:Conflicting attribute names.")
                        return False
                    else:
                        self.attributes.update(k,v)
                return True
    
    
    def get_plugin_from_module(self,module):
        for (k,v) in inspect.getmembers(module):
            if(k.endswith('Plugin')):
                return v()
        return None
    
    
    def unload(self,name):
        (m,p) = self.plugins[name]
        attrib_names = p.get_attribute_types().keys
        
        for a in attrib_names:x
            self.attributes.pop(a)
        
        p.unload(self.cache_dir + '/' + m.__name__)
        self.plugins.pop(m.__name__)
    
    def getPluginIter(self):
        return list(self.plugins.values())
