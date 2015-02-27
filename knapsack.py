import sys
n, W = map(int, sys.stdin.readline().split()) #I hope this is pythonic enough. I tried!
#I tried to minimize global variables, but I felt this was too much to pass into the function
w = [0]*n #item weights
v = [0]*n #item values
c = [0]*n #item copies
j = [0]*n #items used of each
for i in range(n):
        w[i],v[i],c[i] = map(int, sys.stdin.readline().split())
sack = {}
def knap(W,i):
        if W==0:
                return 0,[]
        if i==-1:
                return 0,[]
        if (W,i) not in sack:
		bag=[]
		for j in range(c[i]+1):	
	                if w[i]*j <= W:
        	                t = knap(W-w[i]*j,i-1)
                	        bag.append((t[0]+j*v[i],t[1]+[i for x in range(j)]))
		sack[(W,i)] = max(bag)
		print sack[(W,i)]
        return sack[(W,i)]

ans = knap(W,n-1)
print ans[0]
for x in ans[1]:
	j[x]+=1
print j
