from auditor import perceptron,string_enc

class PerceptronClassifier():
    
    def __init__(self,fData):
        self.fTree = fData
        self.enc = string_enc.enc_str_unit
    
    def classify(self,fl):
        f = self.fTree.get(fl)
        attrs = self.enc_file(f)
        retset = []
        for n,f in self.fTree.folder_iter():
            if f.classify_data.classify(attrs)==1:
                retset += [n+'/'+f.name]
        return retset
        
    def train(self,folder):
        tset = []
        for fldr,fl in self.fTree:
            vals = self.enc_file(fl)
            tset += [(vals,1 if fldr==folder else -1)]
        f = self.fTree.get(folder)
        if(f.classify_data == None):
            f.classify_data = perceptron.Perceptron()
            f.classify_data.init_weights(len(tset[0][0]))#value needed
        f.classify_data.train(tset)

    def train_all(self):
        for n,f in self.fTree.folder_iter():
            self.train(n+'/'+f.name)

    def enc_file(self,f):
        result = []
        for k in f.attributes:
            if isinstance(f.attributes[k],int):
                result += [f.attributes[k]]
            elif isinstance(f.attributes[k],str):
                result += self.enc(f.attributes[k],30)#INSERT REASONABLE MAX LENGTH
        return result
