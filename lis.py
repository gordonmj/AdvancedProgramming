import sys
def lis(i,a,d): #I passed dictionary d, so there's no global variables
    if i==0:
        return 0,""
    if i not in d:
        w=[0]*i
        for j in range(i):
            if a[j]<a[i]:
                t=lis(j,a,d)
                w[j]=t[0]+1,t[1]+a[j]
        d[i]=max(w)
    return d[i]    
  
words = []
#I hope this is right!
for line in sys.stdin:
    if line=="\n":
        break
    words.append("Z"+line[:-1]+"{") #Look, I didn't use +=

for a in words:
    print lis(len(a)-1,a,d={})[1][1:]
