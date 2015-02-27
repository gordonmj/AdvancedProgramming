import math
import random

def find(A,x,k):
    Ax = []
    if x < A[0]:
        return A[:k]
    if x > A[-1]:
        return A[len(A)-k:]
    a = len(A)/2
    b = a+1
    if x > A[a] and x < A[b]:
        for i in range(k):
           # print "A is",A,"a is",a,"b is",b
            if math.fabs(A[a]-x) < math.fabs(A[b]-x):
                Ax+=[A[a]]
                a-=1
            else:
                Ax+=[A[b]]
                if b < len(A)-1:
                    b+=1                   
                else:
                    b = a-1
    elif x < A[a]:
        return find(A[:len(A)/2],x,k)
    else:
        return find(A[len(A)/2:],x,k)
    return Ax

print find([1,2,3,4,4,7],5.2,2) #[4,4]
print find([1,2,3,4,4,7],6.5,3) #[7,4,4]
#print find([1,1,1,1,1,1,1,1,1,1,1],0.7,3)
