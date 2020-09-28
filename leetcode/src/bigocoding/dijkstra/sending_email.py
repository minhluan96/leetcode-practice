import heapq


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


class Solution:
    def dijkstra(self, start):
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

    def sending_email(self, start, end):
        self.dijkstra(start)
        if dist[end] != INF:
            return dist[end]

        return 'unreachable'


if __name__ == '__main__':
    Q = int(input())
    INF = int(1e9)
    counter = 0
    for i in range(Q):
        counter += 1
        N, M, S, T = list(map(int, input().split()))

        graph = [[] for _ in range(N)]
        dist = [INF for _ in range(N)]

        for _ in range(M):
            i, j, w = list(map(int, input().split()))
            graph[i].append(Node(j, w))
            graph[j].append(Node(i, w))

        solution = Solution()
        result = solution.sending_email(S, T)
        print('Case #{}: {}'.format(counter, result))

