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

            if not visited[v] and w * p < dist[v]:
                dist[v] = w * p
                heapq.heappush(pq, Node(v, w * p))

def totalMST():
    total = 0
    for i in range(n + 1):
        if dist[i] == INF:
            continue
        total += dist[i]

    print(total)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p = int(input())
        n = int(input())
        m = int(input())

        INF = int(1e9)
        graph = [[] for _ in range(n + 1)]
        dist = [INF for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]

        for _ in range(m):
            a, b, c = map(int, input().split())
            graph[a].append(Node(b, c))
            graph[b].append(Node(a, c))

        start = 1
        prims(start)
        totalMST()

