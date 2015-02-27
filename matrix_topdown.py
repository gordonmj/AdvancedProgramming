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

def matrix(p):
    n = len(p) - 1
    for i in range(1,n+1):
        for j in range(i,n+1):
            m[i,j] = 100000
    print matrix2(p,1,n), parens(1,n)

def matrix2(p,i,j):
    if m[i,j] < 100000:
        return m[i,j]
    if i==j:
        m[i,j]=0
    else:
        for k in range(i,j):
            m1 = matrix2(p,i,k)
            m2 = matrix2(p,k+1,j)
            q = m1+m2+p[i][0]*p[k][1]*p[j][1]
            if q < m[i,j]:
                m[i,j] = q
                b[i,j] = k
    return m[i,j]

def parens(i,j):
    rs = ''
    if i==j:
        rs += 'A'+str(i)
    else:
        rs += '('
        rs += parens(i,b[i,j])
        rs += parens(b[i,j]+1,j)
        rs += ')'
    return rs

for line in lines:
    m = defaultdict(int)
    b = defaultdict(int)
    matrix(line)
            

