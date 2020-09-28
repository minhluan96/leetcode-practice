'''
Solution
'''

import heapq

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist


class Solution:
    def dijkstra(self, start, graph, dist):
        pq = []
        heapq.heappush(pq, Node(start, 0))
        dist[start] = 0

        while len(pq):
            top = heapq.heappop(pq)
            u = top.id
            w = top.dist

            for neigh in graph[u]:
                if w + neigh.dist < dist[neigh.id]:
                    dist[neigh.id] = w + neigh.dist
                    heapq.heappush(pq, Node(neigh.id, dist[neigh.id]))

    def almost_shortest_path(self):
        distS = [INF for _ in range(N)]
        distD = [INF for _ in range(N)]
        dist = [INF for _ in range(N)]

        self.dijkstra(S, graphS, distS)
        self.dijkstra(D, graphD, distD)

        shortest_dist = distS[D]

        for u in range(N):
            for neigh in graphS[u]:
                v = neigh.id
                w = neigh.dist
                if distS[u] + w + distD[v] != shortest_dist:
                    almost_graph[u].append(Node(v, w))

        self.dijkstra(S, almost_graph, dist)
        if dist[D] == INF:
            print(-1)
        else:
            print(dist[D])


if __name__ == '__main__':

    while True:
        N, M = list(map(int, input().split()))
        if N == 0 and M == 0:
            break
        S, D = list(map(int, input().split()))
        INF = int(1e9)

        graphS = [[] for _ in range(N)]
        graphD = [[] for _ in range(N)]
        almost_graph = [[] for _ in range(N)]

        for _ in range(M):
            u, v, w = list(map(int, input().split()))
            graphS[u].append(Node(v, w))
            graphD[v].append(Node(u, w))

        solution = Solution()
        solution.almost_shortest_path()


