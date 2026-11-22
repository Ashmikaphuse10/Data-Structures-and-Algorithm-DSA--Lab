from collections import deque

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def display(self):
        print("\nAdjacency List:")
        for i in range(self.v):
            print(i, "->", self.adj[i])

    def bfs(self, start):
        if start < 0 or start >= self.v:
            print("Invalid starting vertex")
            return []

        visited = [False] * self.v
        q = deque([start])
        visited[start] = True
        result = []

        while q:
            vertex = q.popleft()
            result.append(vertex)

            for neighbour in sorted(self.adj[vertex]):
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)

        return result


n = int(input("Enter number of vertices: "))
g = Graph(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge: ").split())
    g.add_edge(u, v)

g.display()

start = int(input("Enter starting vertex for BFS: "))
result = g.bfs(start)

if result:
    print("BFS Traversal:", *result)

    if len(result) < n:
        print("Unreachable vertices:", end=" ")
        for i in range(n):
            if i not in result:
                print(i, end=" ")