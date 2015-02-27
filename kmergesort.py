import heapq
import random

def mergesorted(a,k):
   # print a
    if len(a)<=1:
        return a
    merged=[]
    heapk =[]
    inq = {}
  #  print a
    for i in range(len(a)):
    #    print a
    #    print i
    #    print a[i]
        if a[i]!=[]:
            heapq.heappush(heapk,[a[i][0],i,0])
    #    print heapk
        inq[i,0]=True
    for i in range(len(a)):
        for j in range(len(a[i])):
            mink, x, y = heapq.heappop(heapk)
   #         print min, x, y
            merged+=[mink]
            if(x,y+1) not in inq and len(a[x])>y+1:
                heapq.heappush(heapk,[a[x][y+1],x,y+1])
                inq[x,y+1]=True
            if(x+1,y) not in inq and len(a)>x+1 and len(a[x+1])>y:
                heapq.heappush(heapk,[a[x+1][y],x+1,y])
                inq[x+1,y]=True
    return merged

def kmergesort(a,k):
   # size = len(a)
    if len(a) <= 1:
        return a
   # while len(a)%3!=0:
   #     a+=[[]]
    klist = []
    for i in range(k):
        klist+=[kmergesort(a[i::k],k)]
   # print klist
    return mergesorted(klist,k)

def randFill(a,k):
   for x in range(k*k):
      a[x]+=random.randint(0,k*k)
   return a

print kmergesort([4,1,5,2,6,3,7,0], 3) 
print kmergesort([4,1,5,2,6,3,7,0,8],4)
print kmergesort([4,1,5,2], 5) 
