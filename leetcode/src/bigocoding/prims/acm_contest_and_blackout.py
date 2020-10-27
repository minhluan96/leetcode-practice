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

            if used[u][v][w] == -1:
                continue

            if not visited[v] and w < dist[v]:
                dist[v] = w
                heapq.heappush(pq, Node(v, w))

def init():
    for i in range(1, N + 1):
        used[i][path[i]][dist[i]] = 1

def getSpanningTree():
    total = 0
    for i in range(1, N + 1):
        total += dist[i]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        INF = int(1e9)
        graph = [[] for _ in range(N + 1)]
        dist = [INF for _ in range(N + 1)]
        visited = [False for _ in range(N + 1)]
        path = [-1 for _ in range(N + 1)]
        used = [None for _ in range(N + 1)]


        for _ in range(M):
            a, b, c = map(int, input().split())
            graph[a].append(Node(b, c))
            graph[b].append(Node(a, c))

        prims(1)
        init()
        min1 = getSpanningTree()
        min2 = INF

        for i in range(1, M):
            u, v, w = edges[i]
            if used[u][v][w] == 1:
                used[u][v][w] = used[v][u][w] = -1
                prims(u)
                min2 = min(min2, getSpanningTree())
                used[u][v][w] = used[v][u][w] = 1

        print(min1, min2)