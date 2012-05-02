

def levenshteinDist(a,b):
    m = len(a)+1
    n = len(b)+1

    if m==1 or n==1:
        return max(m,n)-1

    d = [0]*m
    for i in range(m):
        d[i] = [0]*n
    
    for i in range(m):
        d[i][0] = i
    
    for j in range(n):
        d[0][j] = j
    
    for j in range(1,n):
        for i in range(1,m):
            if(a[i-1] == b[j-1]):
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+1)
    
    return d[m-1][n-1]
