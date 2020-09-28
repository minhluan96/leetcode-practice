class Solution:
    def bellman_ford(self, start):
        dist[start] = 0
        for i in range(1, n):
            for j in range(m):
                u = graph[j][0]
                v = graph[j][1]
                w = graph[j][2]

                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for i in range(1, n):
            for j in range(m):
                u = graph[j][0]
                v = graph[j][1]
                w = graph[j][2]

                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = -INF

    def single_source_shortest_path(self, start, queries):
        self.bellman_ford(start)
        for q in queries:
            if dist[q] == INF:
                print('Impossible')
            elif dist[q] == -INF:
                print('-Infinity')
            else:
                print(dist[q])


if __name__ == '__main__':
    while True:
        n, m, q, s = map(int, input().split())

        if n == 0 and m == 0 and q == 0 and s == 0:
            break

        INF = int(1e9)
        graph = []
        dist = [INF for _ in range(n)]
        for _ in range(m):
            u, v, w = list(map(int, input().split()))
            graph.append((u, v, w))

        queries = []
        for _ in range(q):
            queries.append(int(input()))

        solution = Solution()
        solution.single_source_shortest_path(s, queries)
        print()
