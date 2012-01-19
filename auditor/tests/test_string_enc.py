from .perceptron import Perceptron
from .string_enc import enc_str_unit,enc_str_single    

def test():
    test_data = ["abc","def","h jk","abc","ts"]*20
    test_rez  = [1,-1,-1,1,-1]*20
    per = Perceptron()
    per.init_weights(512)
    per.train(zip(map(lambda x:enc_str_unit(x,4),test_data),test_rez))
    return per
