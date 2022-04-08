from typing import List


class Vertex:
    __slots__ = '_elements'

    def __init__(self, x):
        self._elements = x

    def elements(self):
        return self._elements

    def __hash__(self):
        return hash(id(self))


class Edge:
    __slots__ = '_origin', '_destination', '_elements'

    def __init__(self, origin, destination, elements):
        self._origin = origin
        self._destination = destination
        self._elements = elements

    def endpoints(self):
        return self._origin, self._destination

    def opposite(self, v):
        return self._destination if self is v else self._origin

    def elements(self):
        return self._elements

    def __hash__(self):
        return hash((self._origin, self._destination))


class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for _map in self._outgoing.values():
            result.update(_map.values())
        return result

    def get_edges(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return adj[v]

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v]:
            yield edge

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x):
        edge = Edge(u, v, x)
        self._outgoing[u] = v
        self._incoming[v] = u
