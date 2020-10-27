import math
import heapq

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
    for i in range(N):
        if dist[i] == INF:
            continue
        total += dist[i]
    print("{:.2f}".format(total))

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        input()
        N = int(input())
        INF = int(1e9)
        graph = [[] for _ in range(N)]
        dist = [INF for _ in range(N)]
        visited = [False for _ in range(N)]
        freckles = []
        distances = [None for _ in range(N)]

        for i in range(N):
            x, y = map(float, input().split())
            distances[i] = (x, y)

        for i in range(N - 1):
            for j in range(i + 1, N):
                distI = distances[i]
                distJ = distances[j]
                distance = math.sqrt(pow(distI[0] - distJ[0], 2) + pow(distI[1] - distJ[1], 2))
                graph[i].append(Node(j, distance))
                graph[j].append(Node(i, distance))

        start = 0
        prims(start)
        totalMST()
        if tc != T - 1:
            print()
