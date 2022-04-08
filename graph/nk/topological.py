import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None
        self.in_degree = 0
        self.out_degree = 0


class Graph:
    def __init__(self):
        self.vertex_dictionary = {}
        self.num_vertices = 0

