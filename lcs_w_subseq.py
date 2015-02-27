import sys
from collections import defaultdict
from random import randint

opt = defaultdict(int)
back = defaultdict(int)

def lcs(x, y, z):
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            for k in range(1,len(z)+1):
                if x[i-1] == y[j-1] and x[i-1] == z[k-1]:
                    opt[i,j,k] = opt[i-1,j-1,k-1]+1
                    back[i, j, k] = 1
                elif x[i-1] == y[j-1] and x[i-1] != z[k-1]:
                    opt[i,j,k] = opt[i-1,j-1,k]
                    back[i, j, k] = 2
                else:
                    if opt[i-1,j,k] > opt[i,j-1,k]:
                        opt[i,j,k] = opt[i-1,j,k]
                        back[i,j,k] = 3
                    else:
                        opt[i,j,k] = opt[i,j-1,k]
                        back[i,j,k] = 4
    return opt[i, j, k]

def backtrace(i, j, k):
    if i == 0 or j == 0:
        return ""
    if back[i, j, k] == 1:
        return backtrace(i-1, j-1, k-1) + x[i-1]
    elif back[i, j, k] == 2:
        return backtrace(i-1,j-1,k) + x[i-1]
    elif back[i, j, k] == 3:
        return backtrace(i-1, j, k)
    else:
        return backtrace(i, j-1, k)
inputs = []
line = ""
while line != "\n":
    line = sys.stdin.readline()
    inputs.append(line)

for line in inputs[:-1]:
    x, y, z = line.split()
    opt = defaultdict(int)
    back = defaultdict(int)
    ans = lcs(x,y,z)
    if ans == 0:
        print "NO LCS"
    else:
        print backtrace(len(x),len(y),len(z))
