class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(v):
            visited.add(v)
            result.append(v)
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                result.append(v)
                queue.extend(neighbor for neighbor in self.graph.get(v, []) if neighbor not in visited)

        return result

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

print("DFS:", g.dfs(1))
print("BFS:", g.bfs(1))
