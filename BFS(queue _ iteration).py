from collections import defaultdict
from collections import deque
def bfs(g,s,v,p):
    q = deque()
    p.append(s)
    q.append(s)
    v[s] = True
    while len(q)!= 0:
        tmp = q.popleft()
        for i in g[tmp]:
            if v[i] == False:
                p.append(i)
                q.append(i)
                v[i] = True
    return p


v, e = map(int, input().split())
g = defaultdict(list)
for i in range(e):
    s, d = map(str, input().split())
    g[s].append(d)
    g[d].append(s)

p = []
v = defaultdict(bool)
s = 'A'
print(bfs(g,s,v,p))
