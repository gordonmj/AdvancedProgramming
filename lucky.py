"""
This program passed the first 20 codeforces tests, which, as of this writing, is the best in the class.
"""
import sys
import time
def lcs(i,j,k,a,d):
    x,y,z=a
    if i==-1:
        return 0,""
    if j==-1:
        return 0,""
    if k==-1:
        return 0,""
    if (i,j,k) not in d:
        w=[(0,"")]*3
        if x[i]==y[j] and x[i]==z[k]:
            t=lcs(i-1,j-1,k-1,a,d)
           # print z[:k], t[1][-t[0]:], t[1]
            if z[:k] == t[1][-t[0]:]:
                w[0]=t[0],t[1]
            #    print w[0]
            else:
                t=lcs(i-1,j-1,k,a,d)
                w[0]=t[0]+1,t[1]+x[i]
        elif x[i]==y[j] and x[i]!=z[k]:
            t=lcs(i-1,j-1,k,a,d)
            w[0]=t[0]+1,t[1]+x[i]
        w[1]=lcs(i-1,j,k,a,d)
        w[2]=lcs(i,j-1,k,a,d)
        d[(i,j,k)]=max(w)
    return d[(i,j,k)]
timea = time.time()
words=[raw_input() for x in range(3)]
r=lcs(len(words[0])-1,len(words[1])-1,len(words[2])-1,words,d={})
if r[0]==0:
    print "0"
else:
    print r[1]
#    print "Time to complete: ",time.time()-timea
