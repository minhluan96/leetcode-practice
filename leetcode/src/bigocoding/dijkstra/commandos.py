import heapq


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


class Solution:
    def dijkstra(self, start, dist):
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

    def commandos(self, buildings, start, end):
        distStart = [INF for _ in range(N)]
        distEnd = [INF for _ in range(N)]
        self.dijkstra(start, distStart)
        self.dijkstra(end, distEnd)

        totalTimeNeedToComplete = 0
        for k in range(buildings):
            totalTimeNeedToComplete = max(distStart[k] + distEnd[k], totalTimeNeedToComplete)

        return totalTimeNeedToComplete


if __name__ == '__main__':
    T = int(input())
    counter = 0
    INF = int(1e9)

    for _ in range(T):
        counter += 1
        N = int(input())
        R = int(input())
        graph = [[] for _ in range(N)]


        for _ in range(R):
            i, j = list(map(int, input().split()))
            graph[i].append(Node(j, 1))
            graph[j].append(Node(i, 1))

        s, d = list(map(int, input().split()))

        solution = Solution()
        result = solution.commandos(N, s, d)
        print('Case {}: {}'.format(counter, result))
