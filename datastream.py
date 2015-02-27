import sys
import heapq

def mergesorted(a, b):
    if a == [] or b == []:
        return a + b
    if a[0] < b[0]:
        return [a[0]] + mergesorted(a[1:], b)
    return [b[0]] + mergesorted(a, b[1:])

def mergesort(a):
    if len(a) <= 1:
        return a
    left, right = a[:len(a)/2], a[len(a)/2:]
    return mergesorted(mergesort(left), mergesort(right))

def neg(a):
    for i in range(len(a)):
       a[i] = -1*a[i]
    return a 

myheap=[]
k = int(sys.stdin.readline())
for i in range(k):
   line= sys.stdin.readline()
   num = int(line)
   heapq.heappush(myheap,-num)
while True:
   line = sys.stdin.readline()
   if line=='\n' or line=='Stop\n':
       break
   num = int(line)
   maxi = heapq.heappop(myheap)
   if -num > maxi:
      heapq.heappush(myheap,-num)
   else:
      heapq.heappush(myheap,maxi)

negate = neg(myheap)
print mergesort(negate)
