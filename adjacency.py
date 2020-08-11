import numpy as np

from typing import Any, List

class Node:
    def __init__(self, value:Any):
        self.value = value
        #Indicate index position of node
        self.i = None

class Graph:
    def __init__(self, vertices:List[Node]):
        self.vertices = vertices
        self.edges = self._build_adyacency_matrix()

    def _build_adyacency_matrix(self):
        """Initialize adjacency matrix of zeros"""
        #Create list of size v
        matrix = [None] * len(self.vertices)
        #Insert list of size v in each element of matrix
        for i in range(len(matrix)):
            #set the index for each vertice
            self.vertices[i].i = i
            matrix[i] = [0] * len(matrix)
        return matrix

    def connect(self, u:Node, v:Node):
        """ Connect node u and v """
        self.edges[u.i][v.i] = 1
        self.edges[v.i][u.i] = 1
    
    def are_connected(self, u:Node, v:Node):
        """Return whether u and v are conected"""
        if u not in self.vertices or v not in self.vertices:
            return False
        return self.edges[u.i][v.i] == 1

    def print_edges(self):
        print('-' * 30)
        for row in self.edges:
            print(' '.join(str(x) for x in row))
            
    def degree(self, u:Node):
        if u not in self.vertices:
            return -1
        return sum(self.edges[u.i])

    def connected_components(self):
        """ Component (i,j) from matrix M**a, is the number of steps between vi and vj"""
        M = np.array(self.edges)
        M_prim = M**(len(self.vertices))
        print('-' * 30)
        print(M_prim) 

a = Node('a') # i: 0
b = Node('b') # i: 1
c = Node('c') # i: 2
d = Node('d') # i: 3
e = Node('e') # i: 4
f = Node('f') # i: 5

# indices: 0, 1, 2, 3, 4, 5
G = Graph([a, b, c, d, e, f])
G.print_edges()

G.connect(a, b)
G.connect(a, c)
G.connect(a, f)

G.connect(b, c)
G.connect(b, a)

G.connect(c, a)
G.connect(c, b)
G.connect(c, d)

G.connect(d, c)
G.connect(d, e)

G.connect(e, d)

G.connect(f, a)

G.print_edges()

G.connected_components()