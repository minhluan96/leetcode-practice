class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Solution:
    def bellman_ford(self, start):
        dist[start] = 0
        for i in range(1, N):
            for j in range(M):
                u = graph[j].source
                v = graph[j].target
                w = graph[j].weight

                if dist[u] != INF and dist[u] + w > dist[v]:
                    dist[v] = dist[u] + w

        for i in range(M):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight

            if dist[u] != INF and dist[u] + w > dist[v]:
                return False
        return True

    def monk_business_day(self):
        start = 1
        res = self.bellman_ford(start)
        if not res:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())

        INF = -int(1e9)
        graph = []
        dist = [INF for _ in range(N + 1)]

        for _ in range(M):
            i, j, C = map(int, input().split())
            graph.append(Edge(i, j, C))

        solution = Solution()
        solution.monk_business_day()

