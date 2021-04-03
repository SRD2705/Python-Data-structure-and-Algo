# Undirected and unweighted graph implementation
# Initialization of graph
# Find all the paths
# Find the shortest path

class graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for s,e in self.edges:
            if s in self.graph_dict:
                self.graph_dict[s].append(e)
            else:
                self.graph_dict[s] = [e]
        print(self.graph_dict)

    def allpaths(self,st,en,p=[]):
        p = p + [st]
        if st == en:
            return [p]
        if st not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[st]:
            if node not in p:
                tmp_path = self.allpaths(node,en,p)
                for i in tmp_path:
                    paths.append(i)
        return paths

    def shortpath(self,st,en,p=[]):
        p = p + [st]
        if st == en:
            return p
        if st not in self.graph_dict:
            return None
        path = None
        for node in self.graph_dict[st]:
            if node not in p:
                tmp_path = self.shortpath(node,en,p)
                if tmp_path:
                    if path is None or len(tmp_path) < len(path):
                        path = tmp_path
        return path


if __name__ == '__main__':
    routes = [('mum', 'par'),('mum', 'dub'),('par','dub'),('par','ny'),('dub','ny'),('ny','tor')]
    route_graph = graph(routes)
    print(route_graph.allpaths('mum','ny'))
    print(route_graph.shortpath('mum','ny'))