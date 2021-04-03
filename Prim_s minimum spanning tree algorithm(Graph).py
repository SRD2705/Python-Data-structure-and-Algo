# Prims algorithm for minimal spanning tree
# Time: O(V^2)
# In prims algo we will create the graph from start
# We always join the minimum weight vertices to create the tree

from collections import defaultdict
import sys
n = int(input())   # Number of vertices
e = int(input())    # Number of edges
g = [[0 for i in range(n)]for j in range(n)]
for i in range(e):
    s,d,w = map(int,input().split())
    g[s][d] = w
    g[d][s] = w     # we do this because of undirected graph

# We are using adjacecy matrix

# It found the minimum weight from the weight list and return its index
def minval(w,mstset,n):
    mini = sys.maxsize
    ind = None
    for i in range(n):
        if w[i] < mini and mstset[i] == False:       # if any weight is less then minimum and that edge is not in the mstset then we choose it
            mini = w[i]
            ind = i
    return ind

def prim(g,n):
    w = [sys.maxsize]*n  # creting an list of n verticess with infinite value in each
    mstset = [False]*n    # we intitalize all values with False because nothing selected for the tree
    parent = [None]*n       # This list is track the parent of the edges
    w[0] = 0                # We make it zero because we have to choose the starting element as the source
    parent[0] = -1
    for i in range(n):
        s = minval(w,mstset,n)    # It is the selected edge
        mstset[s] = True          # We include it in the mstset
        for j in range(n):
            if g[s][j] > 0 and mstset[j] == False and w[j] > g[s][j]:     # We consider all connected vertices
                w[j] = g[s][j]
                parent[j] = s
    for i in range(1,n):
        print(parent[i], " -- ", i, g[i][parent[i]])         # It prints the mst

prim(g,n)


'''
INPUT:
5
7
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
3 4 9
OUTPUT:
0  --  1 2
1  --  2 3
0  --  3 6
1  --  4 5
'''