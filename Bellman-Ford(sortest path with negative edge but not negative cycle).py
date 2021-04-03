# Bellman-Ford algorithm(for shortest path with negative edge but not negative cycle)
# Time: O(VE)
# It use to find the shortest path from source to all vertices
# It also works for the edge with negative weight where Dijkstra's algo does not work for negative edge
# But if negative cycle present in this graph then both Dijkstra's and Bellman-Ford does not work
# Where bellman ford can detect the negative cycle but dijkstra's can not detect it.
# If an undirected graph with negative edge weight found then we can not apply this algorithm
# It only work for directed graph with negative edge and without negative cycle

# We can iterate maximum of v-1 times
# After that if we found that the cost array changes then we know that the graph has a negative cycle

import sys

v = int(input())
g = []


def addedge(s, d, w, g):
    g.append([s, d, w])


def bellman_ford(s):
    cost = [sys.maxsize] * v  # It tracks the cost of all vertices
    cost[0] = 0
    for _ in range(v - 1):
        for s, d, w in g:
            if cost[s] != sys.maxsize and w + cost[s] < cost[d]:  # If we found any cost lesser thank the stored cost then we will update
                cost[d] = w + cost[s]
    for s, d, w in g:
        if cost[s] != sys.maxsize and w + cost[s] < cost[d]:  # It detects the negative cycle
            print("Negative cycle detected")
            return
    for i in range(v):
        print(i, cost[i])


addedge(0, 1, -1, g)
addedge(0, 2, 4, g)
addedge(1, 2, 3, g)
addedge(1, 3, 2, g)
addedge(1, 4, 2, g)
addedge(3, 2, 5, g)
addedge(3, 1, 1, g)
addedge(4, 3, -3, g)
bellman_ford(0)

'''
Input:
5
Output:
0 0
1 -1
2 2
3 -2
4 1
'''
