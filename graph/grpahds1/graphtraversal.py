from graph.grpahds1.graphclasses import Graph, Vertex


def dfs(g: Graph, u: Vertex, discovered):
    for edge in g.incident_edges(u):
        v = edge.opposite(u)
        if v is not discovered:
            discovered[v] = edge
            dfs(g, v, discovered)


def bfs(g: Graph, s: Vertex, discovered):
    level = [s]
    while len(level):
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level


def topological_sort(g: Graph):
    topo = []
    ready = []
    incount = {}
    for u in g.vertices():
        incount[u] = g.degree(u, False)
        if incount[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo
