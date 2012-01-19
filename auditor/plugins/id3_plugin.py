import stagger


class ID3Plugin(BasePlugin):
    '''Plugin that reads ID3 tags.'''
    name    = "ID3 Plugin."
    author  = "Tom Bytheway"
    version = "0.0.0" 
    
    def get_attribute_types(self):
        n = lambda x,y:0
        return {'ARTIST':n,
                'ALBUM' :n,
                'GENRE' :n,
                'YEAR'  :(lambda x,y:1 if x<y else -1)}
    
    def evaluate_file(self,filename,path):
        tags = stagger.read_tag(filename)
        return {'ARTIST':tags.artist,
                'ALBUM':tags.album,
                'GENRE':tags.genre,
                'YEAR':tags.year}
    
    
