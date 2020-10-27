import heapq

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

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

    print(total)


if __name__ == '__main__':
    N, M = map(int, input().split())

    INF = int(1e9)
    graph = [[] for _ in range(N + 1)]
    dist = [INF for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    for i in range(M):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    S = int(input())
    prims(S)
    totalMST()