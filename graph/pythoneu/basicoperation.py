graph = {
    "a": {"c"},
    "b": {"c", "e"},
    "c": {"a", "b", "d", "e"},
    "d": {"c"},
    "e": {"b", "c"},
    "f": {},
}


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append({node, neighbour})
    return edges


def find_isolated_nodes(graph):
    isolated_nodes = []
    for node in graph:
        if not graph[node]:
            isolated_nodes.append(node)
    return isolated_nodes


if __name__ == '__main__':
    edges = generate_edges(graph)
    print(f'edges : {edges}')

    isolated_nodes = find_isolated_nodes(graph)
    print(f'isolated_nodes : {isolated_nodes}')
