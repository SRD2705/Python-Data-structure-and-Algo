# single source shortest path algorithm(Dijkstra's algo)-->Greedy
# all source shortest path algorithm(Floyd-Warshall algo)-->Dynamic programming

from collections import defaultdict
import heapq
def dijkstra(g,s,d):
    h = []                  # It keep track the record of the tracks with costs
    heapq.heappush(h,(0,s)) # It always pop the minimum cost
    while len(h)!=0:        # Greedy src --> min --> min --> des
        curcost,curpos = heapq.heappop(h)
        if curpos == d:
            print(curcost)
            break
        for neigh,cost in g[curpos]:
            heapq.heappush(h,(curcost+cost, neigh))


g = defaultdict(list)
v,e = map(int, input().split())
for i in range(e):
    s,d,w = map(str, input().split())
    g[s].append((d, int(w)))
src, des = map(str, input().split())
dijkstra(g,src,des)
'''
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
A D
'''