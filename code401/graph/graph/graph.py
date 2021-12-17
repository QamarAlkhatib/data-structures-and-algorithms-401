class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_node(self,value):
        node = Vertex(value)
        self.__adjacency_list[node] = []
        return node
        

    def add_edge(self, node1, node2, weight=0):
   
        if node1 not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")
        
        if node2 not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(node2, weight)
        self.__adjacency_list[node1].append(edge)

    def get_nodes(self):
        return self.__adjacency_list.keys()

    def get_neighbors(self,node):
        return self.__adjacency_list.get(node,[])

    def get_sizes(self):
        return len(self.__adjacency_list)

    def print_adj(self):
        for node in self.__adjacency_list:
            print(node.value,":", self.__adjacency_list[node])


