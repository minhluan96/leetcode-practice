class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Solution:
    def bellman_ford(self, start):
        dist[start] = 100

        for i in range(1, n):
            for j in range(m * 2):
                u = graph[j].source
                v = graph[j].target
                w = graph[j].weight

                if (dist[u] != INF) and (dist[u] * w / 100 > dist[v]):
                    dist[v] = dist[u] * w / 100
                    path[v] = u

    def to_chicago(self):
        start = 1
        self.bellman_ford(start)
        return "{:.6f}".format(dist[n]) + ' percent'


if __name__ == '__main__':
    while True:
        lines = list(map(int, input().split()))
        if len(lines) == 1 and lines[0] == 0:
            break

        n, m = lines[0], lines[1]

        INF = -int(1e9)
        graph = []
        dist = [INF for _ in range(n + 1)]
        path = [-1 for _ in range(n + 1)]

        for _ in range(m):
            u, v, w = list(map(int, input().split()))
            graph.append(Edge(u, v, w))
            graph.append(Edge(v, u, w))

        solution = Solution()
        result = solution.to_chicago()

        print(result)