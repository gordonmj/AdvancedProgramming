import sys
from collections import defaultdict

N = input()
AllTops = []
AllEdges = []
AllVs = []
#Top sort
for g in range(N):
    V, E = map(int, sys.stdin.readline().split())
    edgeline = sys.stdin.readline()
    edges =  []
    #print edgeline
    for e in range(E):
        x = int(edgeline[1])
        y = int(edgeline[4])
        edges.append((x,y))
        edgeline = edgeline[7:]
    deg = [0]*(V+1)
    idz = [0]*(V+1) #indegree zero nodes
    top = []
    for v in range(1,V+1):
        for e in range(E):
            if edges[e][1] == v:
                deg[v]+=1
    change = True
    while change:
        change = False
        for v in range(1,V+1):
            if deg[v]==0:
               top.append(v)
               deg[v] = -1
               change = True
               for v2 in range(1,V+1):
                   for e in range(E):
                       if edges[e][0] == v and edges[e][1] == v2:
                           if deg[v2] > 0:
                               deg[v2] -= 1
    AllTops.append(top)
    AllEdges.append(edges)
    AllVs.append(V)
for g in range(N):
    if len(AllTops[g]) < V:
        print "CYCLIC"
    else:
        opt = defaultdict(int)
        back = defaultdict(int)
        #Viterbi
        opt[1] = 1
        for v in AllTops[g]:
            for e in AllEdges[g]:
                if e[1] == v:
                    u = e[0]
                    opt[v] = opt[v] + opt[u]
        print opt[AllVs[g]]
