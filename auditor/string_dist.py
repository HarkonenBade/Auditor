

def levenshtienDist(a,b):
    m = len(a)
    n = len(b)

    if m==0 or n==0:
        return max(m,n)

    d = [0]*m
    for i in range(m):
        d[i] = [0]*n
    
    for i in range(m):
        d[i][0] = i
    
    for j in range(n):
        d[0][j] = j
    
    for j in range(1,n):
        for i in range(1,m):
            if(a[i] == b[j]):
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+1)
    
    return d[m-1][n-1]
