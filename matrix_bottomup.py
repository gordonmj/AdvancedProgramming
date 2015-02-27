import sys
from collections import defaultdict

N = input()
lines =[]
for n in range(N):
    s = sys.stdin.readline().split() #read in the line and split
    a = []
    a.append([1,1])
    for t in s: #for each "matrix" dimension
        y = t.replace('x',' ') #switch x to space
        d = y.split() #then split
        a.append((map(int, d))) #append the integer version of those elements
    lines.append(a) #add the whole line of integer elements
    
"""
def matrix(p):
    n = len(p)
    for i in range(n):
        for j in range(i,n):
            m[i,j] = float("inf")
    print matrix2(p)#, parens(0,n - 1)
"""
def matrix2(p):
    n = len(p) - 1
    #print p,n
    for i in range(1,n+1):
        m[i,i] = 0
    #print m
    for l in range(2,n + 1):
        for i in range(1,(n - l) + 2):
            #print "l",l,"i",i,
            j = i + l - 1
            #print j
            m[i,j] = 100000
            for k in range(i,j):
                #print i,k,j
                #print p
                q = m[i,k] + m[k+1,j] + p[i][0]*p[k][1]*p[j][1]
                #print q
                if q < m[i,j]:
                    m[i,j] = q
                    b[i,j] = k
    #!print m[1,n]
    return m[1,n]

def parens(i,j):
    rs = ''
    if i==j:
        rs += 'A'+str(i)
    else:
      #  print "i",i,"j",j,"b[i,j]",b[i,j]
        rs += '('
        rs += parens(i,b[i,j])
        rs += parens(b[i,j]+1,j)
        rs += ')'
    return rs

for line in lines:
    m = defaultdict(int)
    b = defaultdict(int)
    print matrix2(line)
    #print m
    #print b
    print parens(1,len(line)-1)

