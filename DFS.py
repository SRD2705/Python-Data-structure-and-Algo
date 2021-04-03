from collections import defaultdict
def dfs(g,s,v,p):
    p.append(s)
    v[s] = True
    for i in g:
        if v[i] == False:
            dfs(g,i,v,p)
    return p

v, e = map(int, input().split())
g = defaultdict(list)
for i in range(e):
    s, d = map(str, input().split())
    g[s].append(d)
    g[d].append(s)
p = []
s = 'A'
v = defaultdict(bool)
res = dfs(g,s,v,p)

print(g)
print(res)