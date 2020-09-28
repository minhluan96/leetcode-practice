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

    def mice_and_maze(self, N, end, timer):
        counter = 0
        for i in range(1, N + 1):
            dist = [INF for _ in range(N + 1)]
            self.dijkstra(i, dist)
            if dist[end] <= timer:
                counter += 1
        return counter


if __name__ == '__main__':
    N = int(input())
    E = int(input())
    T = int(input())
    M = int(input())

    INF = int(1e9)
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        lines = list(map(int, input().split()))
        graph[lines[0]].append(Node(lines[1], lines[2]))


    solution = Solution()
    result = solution.mice_and_maze(N, E, T)
    print(result)
