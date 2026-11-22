class Graph:
    def __init__(self, n):
        self.n = n
        self.mat = [[0] * n for i in range(n)]

    def add_edge(self, u, v, w):
        self.mat[u][v] = w
        self.mat[v][u] = w

    def display(self):
        print("\nAdjacency Matrix:")
        for row in self.mat:
            print(row)

    def prim(self, start):
        visited = [False] * self.n
        visited[start] = True
        total = 0

        print("\nMinimum Spanning Tree:")
        print("Edge  Weight")

        for i in range(self.n - 1):
            minimum = 999
            u = -1
            v = -1

            for a in range(self.n):
                if visited[a]:
                    for b in range(self.n):
                        if not visited[b] and self.mat[a][b] != 0:
                            if self.mat[a][b] < minimum:
                                minimum = self.mat[a][b]
                                u = a
                                v = b

            if u == -1:
                print("Graph is disconnected")
                return

            print(u, "-", v, " ", minimum)
            visited[v] = True
            total += minimum

        print("Total Minimum Cost:", total)


n = int(input("Enter number of vertices: "))
g = Graph(n)

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    g.add_edge(u, v, w)

g.display()

start = int(input("Enter starting vertex: "))
g.prim(start)