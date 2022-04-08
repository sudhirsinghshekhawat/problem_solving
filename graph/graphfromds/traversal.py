import heapq

from graph.graphfromds.classes import Graph


def DFS(g: Graph, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v is not discovered:
            discovered[v] = e
            DFS(g, v, discovered)


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


def shortest_path(g: Graph, src):
    d = {}
    cloud = {}
    pq = []
    pqlocator = {}

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = heapq.heappush(pq, (d[v], v))

    while not pq:
        key, u = pq.pop(0)
        cloud[u] = key
        del pqlocator[u]
        for e in g.insert_edge(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v)
