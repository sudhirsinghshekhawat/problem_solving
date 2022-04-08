"""
A simple python graph class
demonstrating the essential facts and functionalities of graphs
"""


class Graph(object):
    def __init__(self, graph_dict=None):
        """
        Initialize the graph dictionary
        if no dictionary or None is given
        an empty dictionary will be used
        :param graph_dict: dictionary
        """
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """
        returns list of all the edges of vertices
        """
        return self._graph_dict[vertice]

    def all_vertices(self):
        """returns the vertices of graph as a set"""
        return set(self._graph_dict.keys())

    def all_edges(self):
        """returning the edges of a graph"""
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex is not in graph then
        key vertex with empty list will be added
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        assume that edge is type set tuple or list
        between 2 vertices
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """
        a static function that will generate the edges of
        graph
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbor in self._graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({neighbor, vertex})
        return edges

    def __iter__(self):
        self.__iter_obj = iter(self._graph_dict)
        return self.__iter_obj

    def __next__(self):
        """allows us to iterate over the object"""
        return next(self.__iter_obj)

    def __str__(self):
        res = "vertices"
        for k in self._graph_dict:
            res += str(k)
        res += "\n edges "
        for edge in self.__generate_edges():
            res += str(edge)
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        """find the path from start vertex to end vertex"""
        if path is None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_path(self, start_vertex, end_vertex, path=[]):
        """
        find all the path from start vertex to end vertex
        """
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_all_path(vertex, start_vertex, end_vertex, path)
                for p in extended_path:
                    paths.append(p)
        return path

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connected it"""
        degree = len(self._graph_dict[vertex])
        if vertex in self._graph_dict[vertex]:
            degree += 1
        return degree

    def bfs(self, vertex, visited=[], queue=[]):
        """breadth first search for graph"""
        visited.append(vertex)
        queue.append(vertex)

        while queue:
            s = queue.pop(0)
            print('s', end=' ')
            for neighbor in self._graph_dict[s]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)


if __name__ == '__main__':
    g = {
        "a": {"c"},
        "b": {"c", "e"},
        "c": {"a", "b", "d", "e"},
        "d": {"c"},
        "e": {"b", "c"},
        "f": {},
    }
    graph = Graph(g)
    for vertice in graph:
        print(f"edges of vertice {vertice} : ", graph.edges(vertice))
