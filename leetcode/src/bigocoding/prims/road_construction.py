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
    for i in range(actualN):
        if dist[i] == INF:
            return -1

        total += dist[i]

    return total

if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        input()
        M = int(input())
        INF = int(1e9)
        N = M * 2

        graph = [[] for _ in range(N)]

        cityMap = {}

        cnt = 0
        for _ in range(M):
            line = input().split()
            city1 = line[0]
            city2 = line[1]
            cost = int(line[2])
            city1Pos, city2Pos = -1, -1
            if city1 not in cityMap:
                cityMap[city1] = cnt
                cnt += 1

            if city2 not in cityMap:
                cityMap[city2] = cnt
                cnt += 1

            city1Pos = cityMap[city1]
            city2Pos = cityMap[city2]
            graph[city1Pos].append(Node(city2Pos, cost))
            graph[city2Pos].append(Node(city1Pos, cost))

        actualN = cnt
        dist = [INF for _ in range(actualN)]
        visited = [False for _ in range(actualN)]

        prims(0)
        totalMin = totalMST()
        if totalMin == -1:
            print('Case {}: Impossible'.format(case + 1))
        else:
            print('Case {}: {}'.format(case + 1, totalMin))


