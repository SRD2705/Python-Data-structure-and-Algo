from collections import defaultdict


class graph:
    def __init__(self, edge):
        self.edge = edge
        self.graph_dict = defaultdict(list)
        for s, e in edge:
            if s not in self.graph_dict:
                self.graph_dict[s] = [e]
            else:
                self.graph_dict[s].append(e)
        print(self.graph_dict)

    def dfs(self, s):
        vis = []
        stack = [s]
        while stack:
            s = stack[-1]
            if s not in vis:
                vis.append(s)
                stack.pop()
                for nodes in self.graph_dict[s]:
                    if nodes not in vis:
                        stack.append(nodes)
            else:
                stack.pop()
                for nodes in self.graph_dict[s]:
                    if nodes not in vis:
                        stack.append(nodes)
        return vis

    def bfs(self, s):
        vis = []
        q = [s]
        while q:
            s = q[0]
            if s not in vis:
                vis.append(s)
                q.pop(0)
                for node in self.graph_dict[s]:
                    if node not in vis:
                        q.append(node)
            else:
                q.pop(0)
                for node in self.graph_dict[s]:
                    if node not in vis:
                        q.append(node)
        return vis




if __name__ == '__main__':
    v, e = map(int, input().split())
    routes = []
    for i in range(e):
        sd = list(map(int, input().split()))
        routes.append(sd)
    tmp = [('mum', 'par'), ('mum', 'dub'), ('par', 'dub'), ('par', 'ny'), ('dub', 'ny'), ('ny', 'tor')]
    #g = graph(routes)
    g1 = graph(tmp)
    print(g1.dfs('mum'))
    print(g1.bfs('mum'))
    #print(g.dfs('mum'))
    #print(g.bfs('mum'))
    #print(g.toposort())

'''
5 7
1 3
1 4
2 1
2 4
3 5
4 3
4 5
'''
