class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Solution:
    def bellman_ford(self, start):
        dist[start] = 0

        for i in range(1, n):
            for j in range(len(graph)):
                u = graph[j].source
                v = graph[j].target
                w = graph[j].weight

                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    def maelstrom(self):
        start = 1
        self.bellman_ford(start)

        maxVal = 0
        for val in dist:
            if val != INF and maxVal < val:
                maxVal = val

        return maxVal

'''
minimum communication time required to broadcast a message from the first processor to all the other processors.
~> which mean the largest time that to run all over the processes
'''
if __name__ == '__main__':
    n = int(input())

    INF = int(1e9)
    graph = []
    dist = [INF for _ in range(n + 1)]

    des = 1
    for p in range(2, n + 1):
        lines = list(input().split())
        for q in range(len(lines)):
            weight = INF if lines[q] == 'x' else int(lines[q])

            graph.append(Edge(p, q + 1, weight))
            graph.append(Edge(q + 1, p, weight))

    solution = Solution()
    ans = solution.maelstrom()
    print(ans)