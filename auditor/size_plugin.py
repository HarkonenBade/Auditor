from base_plugin import BasePlugin
import os,math


class SizePlugin(BasePlugin):
    '''Plugin to classify files based on size.'''
    
    name = "Size Classifier."
    author = "Tom Bytheway"
    version = "0.0.1"
    
    def load(self,cachedir):
        pass
    
    def unload(self,cachedir):
        pass
    
    def get_attribute_types(self):
        return {"Size":self.size_order}
    
    def evaluate_file(self,filename,path):
        size = os.path.getsize(filename)
        return {"Size":size}
    
    def size_order(self,f1,f2):
        return math.floor(min(max(f1-f2,-1),1)) #Returns 1 if f1>f2, 0 if f1=f2 and -1 if f2>f1