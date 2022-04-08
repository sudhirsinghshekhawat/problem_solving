from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.N = n

    def add_edge(self, m, n):
        self.graph[m].append(n)

    def sort_util(self, n, visited, stack):
        visited[n] = True
        for element in self.graph[n]:
            if not visited[element]:
                self.sort_util(element, visited, stack)
        stack.insert(0, n)

    def topological_sort(self):
        visited = [False] * self.N
        stack = []

        for element in range(self.N):
            if not visited[element]:
                self.sort_util(element, visited, stack)
        print(stack)


if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.topological_sort()
