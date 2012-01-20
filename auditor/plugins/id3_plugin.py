from auditor.string_dist import levenstienDist
import stagger


class ID3Plugin(BasePlugin):
    '''Plugin that reads ID3 tags.'''
    name    = "ID3 Plugin."
    author  = "Tom Bytheway"
    version = "0.0.0" 
    
    def get_attribute_types(self):
        n = lambda x,y:0
        return {'ARTIST':levenstienDist,
                'ALBUM' :levenstienDist,
                'GENRE' :levenstienDist,
                'YEAR'  :lambda x,y:abs(x-y)}
    
    def evaluate_file(self,filename,path):
        tags = stagger.read_tag(filename)
        return {'ARTIST':tags.artist,
                'ALBUM':tags.album,
                'GENRE':tags.genre,
                'YEAR':tags.year}
    
    
