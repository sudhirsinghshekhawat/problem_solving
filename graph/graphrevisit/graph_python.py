class Vertex:
    """Light weight  vertex structure of graph"""
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self) -> int:
        return hash(id(self))


class Edge:
    """Light weight edge structure of graph"""

    __slots__ = "_origin", "_destination", "_element"

    def __init__(self, u, v, x):
        """
        Do not call it directly, use the method
        Graph's insert edge method
        """
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        """ Return (u,v) tuple of vertices """
        return (self._origin, self._destination)

    def opposite(self, v):
        """ Return vertex that is opposite of v"""
        return self._destination if v is self else self._origin

    def element(self):
        """ Return element associated with this edge """
        return self._element

    def __hash__(self):
        return hash(self._origin, self._destination)


class Graph:
    """
    Representation of Simple Graph using adjency map
    """

    def __init__(self, directed=False):
        """
        Create an Empty graph(undirected by default)
        Graph is directed if optional param is set to True
        Args:
            directed (bool, optional): [description]. Defaults to False.
        """
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True if directed graph else Return False"""
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """ Return number of vertices in graph """
        return len(self._outgoing)

    def vertices(self):
        """ Return all the vertices """
        return self._outgoing.keys()

    def edge_count(self):
        """ Return the total edges of Graph """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        """ Return the set of all edges in the graph """
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Return the all edges from u to v , or none if not adjacent """
        return self._outgoing[u].get(v)

    def degree(self, v, out_going=True):
        adj = self._outgoing if out_going else self._incoming
        return len(adj)

    def incident_edges(self, v, outgoing=True):
        """ Return edges which are incident to vertex v
        if graph is directed optional parameter is used to request incoming edges
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
