import heapq
import math

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def prims(start):
    pq = []
    heapq.heappush(pq, Node(start, 0))
    dist[start] = 0

    while len(pq):
        top = heapq.heappop(pq)
        u = top.id
        visited[u] = True

        for neigh in graph[u]:
            v = neigh.id
            w = neigh.dist

            if not visited[v] and w < dist[v]:
                dist[v] = w
                heapq.heappush(pq, Node(v, w))


def totalMST():
    total = 0
    for i in range(N + 1):
        if dist[i] == INF:
            continue
        total += dist[i]

    print("{:.2f}".format(total))


if __name__ == '__main__':
    while True:
        try:
            N = int(input())

            INF = int(1e9)
            graph = [[] for _ in range(N + 1)]
            dist = [INF for _ in range(N + 1)]
            visited = [False for _ in range(N + 1)]

            distances = [None for _ in range(N + 1)]
            for i in range(N):
                x, y = map(int, input().split())
                distances[i + 1] = (x, y)

            for i in range(1, N + 1):
                for j in range(i + 1, N + 1):
                    distI = distances[i]
                    distJ = distances[j]
                    distance = math.sqrt(pow(distI[0] - distJ[0], 2) + pow(distI[1] - distJ[1], 2))
                    graph[i].append(Node(j, distance))
                    graph[j].append(Node(i, distance))

            M = int(input())
            start = -1
            for i in range(M):
                u, v = map(int, input().split())
                distanceU = distances[u]
                distanceV = distances[v]
                start = u

                graph[u].append(Node(v, 0))
                graph[v].append(Node(u, 0))

            prims(start)
            totalMST()

        except EOFError:
            break
