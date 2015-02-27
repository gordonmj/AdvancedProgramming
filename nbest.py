#Homework 2, question 1
import time
import random
import sys
import math
import heapq
sys.setrecursionlimit(1000000)

n = 5000
A = [0]*n
B = [0]*n

#Based on qselect code posted
def qselect(n, a):
    if a == []:
        return []
    piv = random.randint(0, len(a)-1)
    pivot = a[piv]
    pivsum = pivot[0]
    rest = a[:piv] + a[piv+1:]
    left = [x for x in rest if x[0] < pivsum or (x[0]==pivsum and x[1] <= pivot[1])]
    left_size = len(left)
    if n == left_size+1:
        return pivot
    elif n <= left_size: 
        return qselect(n, left)
    else:
        right = [x for x in rest if x[0] >= pivsum or (x[0] == pivsum and x[1] > pivot[1])]
        return qselect(n-left_size-1, right)

#Modified for pairs
def pairsort(a):
    if a == []:
        return []
    piv = a[random.randint(0, len(a)-1)]
    pivsum = piv[0]+piv[1]
    left = [x for x in a if x[0]+x[1] < pivsum or (x[0]+x[1] == pivsum and x[1] <piv[1])]
    right = [x for x in a if x[0]+x[1] >= pivsum or (x[0]+x[1] == pivsum and x[1] > piv[1])]
    return pairsort(left) + [piv] + pairsort(right)

def qsort(a):
    if a == []:
        return []
    piv = a[0]
    left = [x for x in a if x < piv]
    right = [x for x in a[1:] if x >= piv]
    return qsort(left) + [piv] + qsort(right) 

def randFill(a,n):
    timetofill = time.time()
    for x in range(n):
        a[x]=random.randint(0,2*n)

def cart(A,B):
    carttime = time.time()
    AB = []
    for a in A:
      for b in B:
        AB.append((a+b,b,a))
    return AB

def nbesta(a,b):
    ab = cartprod
    timep = time.time()
    sort = sorted(ab)
    C = []
    timex = time.time()
    for i in range(n):
        C+=[[sort[i][2],sort[i][1]]]
    return C

def nbestb(a,b):
    ab = cartprod
    nth = qselect(n,ab)
    C = [x for x in ab if x[0] <= nth[0] or (x[0]==nth[0] and x[1]<=nth[1])]
    Cs = sorted(C)
    Ca = []
    for c in Cs:
        Ca+=[[c[2],c[1]]]
    return Ca[:n]
        
def nbestc(au,bu):
    a = qsort(au)
    b = qsort(bu)
    priorityq = []
    inq ={(0,0):True}
    i=j=0
    heapq.heappush(priorityq,[a[0]+b[0],(a[0],b[0]),i,j])
    nbest=[]
    for x in range(2*n):
        sum, pair, i, j = heapq.heappop(priorityq)
        nbest.append([sum,pair[1],pair[0]])
        if (i,j+1) not in inq and j+1 < len(b):
            heapq.heappush(priorityq,[a[i]+b[j+1],(a[i],b[j+1]),i,j+1])
            inq[i,j+1]=True
        if (i+1,j) not in inq and i+1 < len(a):
            heapq.heappush(priorityq,[a[i+1]+b[j],(a[i+1],b[j]),i+1,j])
            inq[i+1,j]=True
        
    result = sorted(nbest)
    result2 = []
    for x in result:
        result2+=[[x[2],x[1]]]
    return result2[:n]

def printmat(mat):
    for x in mat:
       for y in x:
          print y,
       print

randFill(A,n)
randFill(B,n)
cartprod= cart(A,B)
timeb = time.time()
Cb = nbestb(A,B)
print "Time to run b: "+str(time.time()-timeb)
timec = time.time()
Cc = nbestc(A,B)
print "Time to run c: "+str(time.time()-timec)
timea = time.time()
Ca = nbesta(A,B)
#print "a: ", Ca
#print "b: ", Cb
print "Time to run a: "+str(time.time()-timea)
print "a and b are equal? "+str(Ca == Cb)
#print "c: ", Cc
print "b and c are equal? "+str(Cb == Cc)
print "a and c are equal? "+str(Ca == Cc)

