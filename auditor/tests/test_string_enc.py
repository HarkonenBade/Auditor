from .perceptron import Perceptron

def enc_str_unit(string,m_len):
    ret = []
    for i in range(m_len):
        if(i<len(string)):
            ret.extend([0]*(ord(string[i])-1))
            ret.extend([1])
            ret.extend([0]*(128-ord(string[i])))
        else:
            ret.extend([0]*128)
    return ret

def enc_str_single(string,m_len):
    ret = []
    for i in range(m_len):
        if(i<len(string)):
            ret.extend([ord(string[i])/128])
        else:
            ret.extend([0])
    return ret
    

def test():
    test_data = ["abc","def","h jk","abc","ts"]*20
    test_rez  = [1,-1,-1,1,-1]*20
    per = Perceptron()
    per.init_weights(512)
    per.train(zip(map(lambda x:enc_str_unit(x,4),test_data),test_rez))
    return per
