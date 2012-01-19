import math


class Perceptron():
    
    def __init__(self):
        self.weights = []
        self.training_const = 0.1
        self.min_error = 0.001
    
    def init_weights(self,size):
        self.weights = [0]*(size+1)
    
    def train(self,tset):
        for (i,o) in tset:
            print(self.weights)
            r = self.classify(i)
            print(r)
            print(o)
            deltaw = [self.training_const*(r-o)*x for x in [1]+i]
            print(deltaw)
            for k in range(len(deltaw)):
                if(abs(deltaw[k])>self.min_error):
                    self.weights[k] = self.weights[k]-deltaw[k]
            print(self.weights)
                    
    def classify(self,inputs):
        if self.calc(inputs)>0:
            return 1
        else:
            return -1
    
    def calc(self,inputs):
        return sum([x*y for x,y in zip([1]+inputs,self.weights)])
    
