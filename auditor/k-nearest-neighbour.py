import math

def attrib_dist(f1,f2,pMan):
    dists = 0
    for (n,v) in f1.attributes:
        dist = pMan.attributes[n](f1.attributes[n],f2.attributes[n])
        dists += dist**2
    return math.sqrt(dists)

def k_nearest_neighbour(fName,fDataT,pMan,k):
    nearest_arr = [(0,'')]*k
    curFile = fDataT.get(fName)
    for v,f in fDataT:
        if(f!=curFile):
            dist = attrib_dist(curFile,f,pMan)
            for i in range(k):
                if(nearest_arr[i][0] < dist):
                    for j in range(k-1,i,-1):
                        nearest_arr[j+1] = nearest_arr[j]
                    nearest_arr[i] = (dist,v)
    
