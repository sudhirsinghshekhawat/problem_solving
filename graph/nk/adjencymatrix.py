class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False

    def add_neighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def get_connection(self, G):
        return G.adj_matrix[self.id]

    def get_vertex(self):
        return self.id

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self, num_vertices, cost=0):
        self.adj_matrix = [[-1 for _ in range(num_vertices)]
                           for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        self.vertices = []

        for i in range(0, num_vertices):
            new_vertex = Vertex()
            self.vertices.append(new_vertex)
