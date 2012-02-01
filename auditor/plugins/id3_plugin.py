from auditor.plugins import base_plugin
from auditor.string_dist import levenshtienDist
import stagger


class ID3Plugin(base_plugin.BasePlugin):
    '''Plugin that reads ID3 tags.'''
    name    = "ID3 Plugin."
    author  = "Tom Bytheway"
    version = "0.0.0" 
    
    def get_attribute_types(self):
        return {'ARTIST':levenshtienDist,
                'ALBUM' :levenshtienDist,
                'GENRE' :levenshtienDist,
                'YEAR'  :lambda x,y:abs(x-y)}
    
    def evaluate_file(self,filename,path):
        try:
            tags = stagger.read_tag(path+'/'+filename)
            
            return {'ARTIST':tags.artist,
                    'ALBUM':tags.album,
                    'GENRE':tags.genre,
                    'YEAR':int(tags.date)}
        except ValueError as exc:
            return {'ARTIST':tags.artist,
                    'ALBUM':tags.album,
                    'GENRE':tags.genre,
                    'YEAR':0}
        except Exception as exc:
            return {'ARTIST':'',
                    'ALBUM':'',
                    'GENRE':'',
                    'YEAR':0}
    
    
