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
        self.graph[node1].append((node2,weight))
        # return weight

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
        
def business_trip(g,cities):
    cost = 0
    has_val = False
    for i in range(len(cities)-1):
        neighbors = g.graph[cities[i]]
        for neighbor in neighbors:
          if cities[i+1] == neighbor[0]:
            cost += neighbor[1]
            has_val = True
            break
          else:
            cost += 0
            has_val = False
    if not has_val:
      return False,'$0'     
    return True,'$'+ str(cost)
