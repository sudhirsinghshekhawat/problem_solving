class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False


class Graph:
    def __init__(self, num_vertices, cost=0):
        self.adj_matrix = [[-1 for _ in range(num_vertices)]
                           for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.vertex = []

