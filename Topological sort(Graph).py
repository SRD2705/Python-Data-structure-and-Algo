# Topological sort(using source removal algorithm)
# Need to be DAC(Directed Acyclic Graph)
# For every edge U-->V; U will come before V in ordering of the graph
# InDegree =  Incoming edges on the node
from collections import defaultdict


def topsort(g):
    deg = {}  # For counting the indegree
    for i in g:
        for j in g[i]:
            if j in deg:
                deg[j] += 1
            else:
                deg[j] = 1
    print(deg)
    res = []  # Topological sort ordering
    for i in g:
        if i not in deg:
            res.append(i) # Appending nodes with indegree of Zero
    for i in res:
        for j in g[i]:
            deg[j] -= 1
            if deg[j] == 0:
                res.append(j)
    print(res)


g = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    s, d = map(str, input().split())
    g[s].append(d)
print(g)
topsort(g)

'''
5 7
A C
A D
B A
B D
C E
D C
D E
'''
