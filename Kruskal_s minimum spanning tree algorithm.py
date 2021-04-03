# Kruskal Algorithm for minimum spanning tree
# Time: O(ELogE + ELogV)
# Sorting of edges takes O(ELogE) time.
# After sorting, we iterate through all edges and apply find-union algorithm.
# The find and union operations can take atmost O(LogV) time

def find(parent, i):     # It finds the root parent of the node
    if parent[i] == i:
        return i
    return find(parent,parent[i])


def union(parent, rank, x, y):    # It check the rank and union the sets
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

k = int(input())
g = []
for _ in range(k+1):
    s,d,w = map(int,  input().split())
    g.append([s,d,w])
g = sorted(g, key=lambda i: i[2])  # Sort the list according to the weight of the edges
parent = [i for i in range(k)]
rank = [0] * k
i = 0
e = 0
res = []
cost = 0
while e < k-1:
    u,v,w = g[i]
    i += 1
    x = find(parent,u)
    y = find(parent,v)
    if x != y:
        e += 1
        res.append([u,v,w])
        union(parent,rank,x,y)
for u,v,w in res:
    cost += w
    print(u,"--->",v, "===" ,w)    # We can find the path and only the cost also
print(cost)

'''
Input:
4
0 1 10
0 2 6
0 3 5
1 3 15 
2 3 4
Output:
2 ---> 3 === 4
0 ---> 3 === 5
0 ---> 1 === 10
19
'''