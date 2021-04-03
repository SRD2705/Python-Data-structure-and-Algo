from collections import defaultdict

g = defaultdict(list)
v, e = map(int, input().split())
for i in range(e):
    s, d = map(str, input().split())
    g[s].append(d)
    g[d].append(s)


def bfs(g):
    res = []
    q = ['A']
    while q:
        tmp = q[0]
        if tmp not in res:
            res.append(tmp)
            q.pop(0)
            for node in g[tmp]:
                if node not in res:
                    q.append(node)
        else:
            q.pop(0)
            for node in g[tmp]:
                if node not in res:
                    q.append(node)
    print(res)


def dfs(g):
    res = []
    s = ['A']
    while s:
        tmp = s[-1]
        if tmp not in res:
            res.append(tmp)
            s.pop()
            for node in g[tmp]:
                if node not in res:
                    s.append(node)
        else:
            s.pop()
            for node in g[tmp]:
                if node not in res:
                    s.append(node)
    print(res)


bfs(g)
dfs(g)
'''
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''
