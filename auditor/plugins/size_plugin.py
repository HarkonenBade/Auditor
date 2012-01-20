from .base_plugin import BasePlugin
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
        return {"Size":lambda x,y:abs(x-y)}
    
    def evaluate_file(self,filename,path):
        size = os.path.getsize(filename)
        return {"Size":size}
