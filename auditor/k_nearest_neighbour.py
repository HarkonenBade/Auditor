import math,sys

def attrib_dist(f1,f2,pMan):
    dists = 0
    for n in f1.attributes:
        dist = pMan.attributes[n](f1.attributes[n],f2.attributes[n])
        dists += dist**2
    return math.sqrt(dists)

def k_nearest_neighbour(fName,fDataT,pMan,kVal):
    nearest_arr = [(sys.maxsize,'')]*kVal
    curFile = fDataT.get(fName)
    for v,f in fDataT:
        if(f!=curFile):
            dist = attrib_dist(curFile,f,pMan)
            for i in range(kVal):
                if(nearest_arr[i][0] > dist):
                    nearest_arr.insert(i,(dist,v))
                    nearest_arr.pop()
                    break
#                    for j in range(k-1,i,-1):
#                        nearest_arr[j+1] = nearest_arr[j]
#                    nearest_arr[i] = (dist,v)
    
    majority_rec = {}
    for d,v in nearest_arr:
        if(v in majority_rec):
            majority_rec[v] += 1
        else:
            majority_rec[v] = 1
    
    max_votes = 0
    max_key = ""
    for k,v in majority_rec.items():
        if v>max_votes:
            max_votes = v
            max_key = k
    
    if(max_votes > (kVal/2)):
        return max_key
    else:
        return ''
