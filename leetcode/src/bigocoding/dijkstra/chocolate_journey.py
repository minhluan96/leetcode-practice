import heapq


class Solution:

    def dijsktra(self, start, dist):
        pq = []
        heapq.heappush(pq, (0, start))
        dist[start] = 0

        while len(pq):
            top = heapq.heappop(pq)
            u = top[1]
            w = top[0]
            if dist[u] != w:
                continue

            for neigh in graph[u]:
                if w + neigh[0] < dist[neigh[1]]:
                    dist[neigh[1]] = w + neigh[0]
                    heapq.heappush(pq, (dist[neigh[1]], neigh[1]))

    def chocolate_journey(self, start, end, maxTime):
        self.dijsktra(start, distFromA)
        self.dijsktra(end, distFromB)

        if distFromA[end] == INF:
            return -1

        ans = INF
        for city in cities:
            if distFromB[city] <= maxTime:
                if distFromA[city] != INF and distFromB[city] != INF and ans > distFromA[city] + distFromB[city]:
                    ans = distFromA[city] + distFromB[city]

        if ans == INF:
            return -1

        return ans


if __name__ == '__main__':
    INF = int(1e9)
    N, M, k, x = list(map(int, input().split()))

    cities = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        i, j, d = list(map(int, input().split()))
        graph[i].append((d, j))
        graph[j].append((d, i))

    distFromA = [INF for _ in range(N + 1)]
    distFromB = [INF for _ in range(N + 1)]

    A, B = list(map(int, input().split()))
    solution = Solution()

    result = solution.chocolate_journey(A, B, x)
    print(result)

