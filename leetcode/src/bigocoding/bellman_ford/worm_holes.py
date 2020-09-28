class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Solution:

    def bellman_ford(self, start):
        dist[start] = 0
        for i in range(1, n):
            for j in range(m):
                u = graph[j].source
                v = graph[j].target
                w = graph[j].weight

                if (dist[u] != INF) and (dist[u] + w < dist[v]):
                    dist[v] = dist[u] + w

        for i in range(m):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                return False

        return True

    def worm_holes(self):
        start = 0
        ans = self.bellman_ford(start)
        if not ans:
            print('possible')
        else:
            print('not possible')


if __name__ == '__main__':
    c = int(input())

    for _ in range(c):
        n, m = list(map(int, input().split()))

        graph = []
        INF = int(1e9)

        dist = [INF for _ in range(n)]


        for _ in range(m):
            x, y, t = list(map(int, input().split()))
            graph.append(Edge(x, y, t))

        solution = Solution()
        solution.worm_holes()