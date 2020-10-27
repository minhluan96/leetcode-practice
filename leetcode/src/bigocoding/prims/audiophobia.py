import heapq

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist

def prims(start):
    dist = [INF for _ in range(C + 1)]
    path = [-1 for _ in range(C + 1)]
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
                path[v] = u
                heapq.heappush(pq, Node(v, w))

    for u in range(1, C + 1):
        if path[u] != -1:
            v = path[u]
            w = dist[u]
            graphMST[u].append(Node(v, w))
            graphMST[v].append(Node(u, w))


def dfs(start, end, weight):
    if start == end:
        return weight

    visitedDfs[start] = True
    for p in graphMST[start]:
        v = p.id
        if not visitedDfs[v]:
            temp = dfs(v, end, max(weight, p.dist))
            if temp != INF:
                return temp

    return INF

'''
Cách giải: tìm MST
với mỗi truy vấn, duyệt bfs/dfs để tìm đường đi từ c1 > c2
'''
if __name__ == '__main__':
    case = 1
    while True:
        C, S, Q = map(int, input().split())

        if C == 0 and S == 0 and Q == 0:
            break

        print('Case #{}'.format(case))
        case += 1

        INF = int(1e9)
        graph = [[] for _ in range(C + 1)]
        graphMST = [[] for _ in range(C + 1)]


        for _ in range(S):
            c1, c2, d = map(int, input().split())
            graph[c1].append(Node(c2, d))
            graph[c2].append(Node(c1, d))

        visited = [False for _ in range(C + 1)]

        for i in range(C + 1):
            if not visited[i]:
                prims(i)

        for _ in range(Q):
            visitedDfs = [False for _ in range(C + 1)]
            start, end = map(int, input().split())
            ans = dfs(start, end, 0)
            if ans == INF:
                print('no path')
            else:
                print(ans)
        print()