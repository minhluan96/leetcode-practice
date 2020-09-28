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

                if (dist[u] != INF) and (dist[u] + w < dist[v]):
                    dist[v] = dist[u] + w


    def extended_traffic(self):
        start = 1
        self.bellman_ford(start)

        for des in destinations:
            if dist[des] >= 3 and dist[des] != INF:
                print(dist[des])
            else:
                print('?')


if __name__ == '__main__':
    T = int(input())

    for counter in range(T):
        input()
        INF = int(1e9)

        N = int(input())
        business = list(map(int, input().split()))

        M = int(input())
        graph = []
        dist = [INF for _ in range(N + 1)]

        for _ in range(M):
            u, v = list(map(int, input().split()))
            weight = (business[v - 1] - business[u - 1]) ** 3
            graph.append(Edge(u, v, weight))

        Q = int(input())
        destinations = []
        for _ in range(Q):
            destinations.append(int(input()))

        print('Case {}:'.format(counter + 1))
        solution = Solution()
        solution.extended_traffic()
