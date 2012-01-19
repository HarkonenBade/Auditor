from auditor.plugins.base_plugin import BasePlugin
import os,math


class FakePlugin(BasePlugin):
    '''Fake plugin, classifies all files with the same attribute.'''
    
    name = "Fake Classifier."
    author = "Tom Bytheway"
    version = "0.0.1"
    
    def load(self,cachedir):
        pass
    
    def unload(self,cachedir):
        pass
    
    def get_attribute_types(self):
        return {"FAKE":self.fake_order}
    
    def evaluate_file(self,filename,path):
        return {"FAKE":42}
    
    def fake_order(self,f1,f2):
        return 0
