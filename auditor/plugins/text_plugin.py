from auditor.plugins import base_plugin
import Stemmer,os,operator

PUNCTUATION=",.:;()[]{}-–!\"\n£$%^&+=/\\?~#<>|\t"
NUM_WORDS=20

class TextPlugin(base_plugin.BasePlugin):
    name = "Text Classifier."
    author = "Tom Bytheway"
    version = "0.0.1"
    
    def load(self,cachedir):
        self.stem = Stemmer.Stemmer("english")
        with open("stop.txt","rt") as f:
            self.stop_words = [l.rstrip() for l in f]
    
    def unload(self,cachedir):
        pass
    
    def wordComp(f1,f2):
        matches = 0
        for w in f1:
            if(w != "" and w in f2):
                matches += 1
        return NUM_WORDS-matches
    
    def get_attribute_types(self):
        return {"WORDS":TextPlugin.wordComp}
    
    def evaluate_file(self,filename,path):
        words = []
        with open(os.path.join(path,filename)) as text:
            try:
                for i in range(50):
                    l = text.readline() 
                    if(l==""):
                        break
                    else:
                        words += l.strip(PUNCTUATION).split(" ")
            except e:
                return {"WORDS":[""]*NUM_WORDS}
        
        words = [w for w in words if w != ""]
        
        words = [w for w in words if w.lower() not in self.stop_words]
        
        words = self.stem.stemWords(words)
        
        freq = {}
        for w in words:
            if(w not in freq):
                freq[w]=0
            freq[w] += 1
        
        common_words = [""]*NUM_WORDS
        wl = [(w,freq[w]) for w in freq]
        wl.sort(key=operator.itemgetter(1),reverse=True)
        for (t,i) in zip(wl,range(NUM_WORDS)):
            (w,c) = t
            common_words[i] = w
        
        return {"WORDS":common_words},wl,words
