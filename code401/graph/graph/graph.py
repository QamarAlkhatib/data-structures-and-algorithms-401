class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_node(self,value):
        node = Vertex(value)
        self.graph[node] = []
        return node.value
        

    def add_edge(self, node1, node2, weight=0):
        self.graph[node1].append(node2)

    def get_nodes(self):
        return self.graph.keys()

    def get_neighbors(self,node):
        return self.graph.get(node,[])

    def get_sizes(self):
        return len(self.graph)

    def print_adj(self):
        for node in self.graph:
            print(node,":", self.graph[node])

    def breadth_first(self, node):

        if self.graph[node] is None:
            return None

        if type(node) == str:
            raise Exception
        visited =[False] * len(self.graph)
        result = []

        result.append(node)
        visited[node] = True
        while result:
            node = result.pop(0)
            print(node,end=' ')
            for i in self.graph[node]:
                if visited[i] == False:
                    result.append(i)
                    visited[i] = True



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.breadth_first(0)
# print()
# g.print_adj()
# g.print_adj()s
# a = g.add_node("A")
# b = g.add_node("B")
# g.add_edge(a, b, 10)
# print(g.get_neighbors(a))

