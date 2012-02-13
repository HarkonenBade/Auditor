from auditor.plugins import base_plugin
from auditor.string_dist import levenshtienDist
import subprocess,datetime,pickle

def timeDiff(f1,f2):
    t1 = datetime.datetime.strptime(f1,"%Y:%m:%d %H:%M:%S")
    t2 = datetime.datetime.strptime(f2,"%Y:%m:%d %H:%M:%S")
    delta = t1-t2
    return abs(delta.days)


class EXIFPlugin(base_plugin.BasePlugin):
    '''Plugin to read EXIF data.'''
    name    = "EXIF Plugin."
    author  = "Tom Bytheway"
    version = "0.0.1" 
    
    def get_attribute_types(self):
        '''Retrieves data on all the attributes the plugin supports. Returns a dictionary mapping an attribute type to a function to define distance over that attribute.'''
        return {
               'TIMECAPTURE':timeDiff,
               'CAMMAKE':levenshtienDist,
               'CAMMODEL':levenshtienDist
               }
    
    def evaluate_file(self,filename,path):
        pkl = subprocess.check_output("python2 /home/tom/prj/auditor/plugins/exif.py2 %s"%filename,shell=True)
        ret = {
               'TIMECAPTURE':"",
               'CAMMAKE':"",
               'CAMMODEL':""
              }
        
        if pkl.decode("utf-8") == "":
            return ret
        
        tags = dict([tuple(k.split('#')) for k in pkl.decode("utf-8").rstrip().split("\n")])
        
        if "EXIF DateTimeOriginal" in tags:
            ret["TIMECAPTURE"] = tags['EXIF DateTimeOriginal']
                
        if "Image Make" in tags:
            ret["CAMMAKE"] = tags['Image Make']
                
        if "Image Model" in tags:
            ret["CAMMODEL"] = tags['Image Model']
                
        return ret
