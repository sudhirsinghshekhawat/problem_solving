from collections import deque


class Graph:
    graph_dict = {}  # type: ignore

    def add_edge(self, node, neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
        else:
            self.graph_dict[node].append(neighbor)

    def show_edges(self):
        print(self.graph_dict)

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        for node in self.graph_dict:
            if node in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
                return None

    def BFS(self, s):
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        queue = deque()
        queue.append(s)
        while queue:
            s = queue.popleft()
            for node in self.graph_dict[s]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
            print(s, end=' ')


        


if __name__ == '__main__':
    g = Graph()
    g.add_edge('1', '2')
    g.add_edge('1', '3')
    g.add_edge('2', '3')
    g.add_edge('2', '1')
    g.add_edge('3', '1')
    g.add_edge('3', '2')
    g.add_edge('3', '4')
    g.add_edge('4', '3')

    # g.show_edges()
    print(g.find_path(1, 4))

    g.BFS('1')
