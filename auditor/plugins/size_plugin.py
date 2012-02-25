from auditor.plugins import base_plugin
import os,math


class SizePlugin(base_plugin.BasePlugin):
    '''Plugin to classify files based on size.'''
    
    name = "Size Classifier."
    author = "Tom Bytheway"
    version = "0.0.1"
    
    def load(self,cachedir):
        pass
    
    def unload(self,cachedir):
        pass
    
    def get_attribute_types(self):
        return {"Size":lambda x,y:abs(x-y)}
    
    def evaluate_file(self,filename,path):
        size = math.log(os.path.getsize(os.path.join(path,filename)),2)
        return {"Size":size}
