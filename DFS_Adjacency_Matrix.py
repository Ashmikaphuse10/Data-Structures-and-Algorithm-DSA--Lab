class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.matrix = [[0] * vertices for i in range(vertices)]
        self.visited = [False] * vertices

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def display(self):
        print("\nAdjacency Matrix:")
        for row in self.matrix:
            print(row)

    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")

        for i in range(self.v):
            if self.matrix[vertex][i] == 1 and not self.visited[i]:
                self.dfs(i)


n = int(input("Enter number of vertices: "))
g = Graph(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge: ").split())
    g.add_edge(u, v)

g.display()

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
if 0 <= start < n:
    g.dfs(start)
else:
    print("Invalid vertex")