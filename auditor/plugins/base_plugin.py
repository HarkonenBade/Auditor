


class BasePlugin():
    '''Base class for all plugins.'''
    name    = "Base Plugin."
    author  = "Tom Bytheway"
    version = "0.0.0" 
    
    def load(self,cachedir):
        '''Load method, called when ever the plugin is loaded or reloaded. cachedir is a directory where the plugin can store any cache data it requires.'''
        pass
    
    def unload(self,cachedir):
        '''Unload, called whenever the plugin is reloaded or unloaded. cachedir is a directory where the plugin can store any cache data it requires.'''
        pass
    
    def get_attribute_types(self):
        '''Retrieves data on all the attributes the plugin supports. Returns a dictionary mapping an attribute type to a function to define distance over that attribute.'''
        return {}
    
    def evaluate_file(self,filename,path):
        '''Evaluates a file returning a dictionary mapping attribute types to values for thouse attributes.'''
        pass
    
    
