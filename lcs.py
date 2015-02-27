import sys
import time
def lcs(i,j,x,y,d):
    if i==0:
        return 0,""
    if j==0:
        return 0,""
    if (i,j) not in d:
        w=[(0,"")]*3
        if x[i]==y[j]:
            t=lcs(i-1,j-1,x,y,d)
            w[0]=t[0]+1,t[1]+x[i]
        w[1]=lcs(i-1,j,x,y,d)
        w[2]=lcs(i,j-1,x,y,d)
        d[(i,j)]=max(w)
    return d[(i,j)]

words = []
for line in sys.stdin:
    if line=="\n":
        break
    w1,w2=line.split()
    words.append(("S"+w1+"E","S"+w2+"E"))

for a in words:
    t = time.time()
    r = lcs(len(a[0])-1,len(a[1])-1,a[0],a[1],d={})
    if r[0]==1:
        print "NO LCS"
    else:
        print r[1][:-1]
    print time.time() - t
