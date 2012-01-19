
def enc_str_unit(string,m_len):
    '''Encodes a string as a list of 0's and 1's based on a uniary encoding.'''
    ret = []
    for i in range(m_len):
        if(i<len(string)):
            ret.extend([0]*(ord(string[i])-1))
            ret.extend([1])
            ret.extend([0]*(128-ord(string[i])))
        else:
            ret.extend([0]*128)
    return ret

def enc_str_bin(string,m_len):
    '''Encodes a string as a series of 0's and 1's based on a binary encoding.'''
    ret = []
    for i in range(m_len):
        if(i<len(string)):
            strval = ord(string[i])
            for k in range(7,-1,-1):
                if(strval/(2**k)>=1):
                    strval = strval-(2**k)
                    ret.extend([1])
                else:
                    ret.extend([0])
    return ret

def enc_str_single(string,m_len):
    ret = []
    for i in range(m_len):
        if(i<len(string)):
            ret.extend([ord(string[i])/128])
        else:
            ret.extend([0])
    return ret
