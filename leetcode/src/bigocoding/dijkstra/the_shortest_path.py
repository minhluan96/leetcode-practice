import heapq

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist

class Solution:
    def dijkstra(self, start):
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

    def the_shortest_path(self, start, end):
        self.dijkstra(start)
        return dist[end]


if __name__ == '__main__':
    INF = int(1e9)
    s = int(input())

    for _ in range(s):
        n = int(input())
        city_map = {}
        graph = [[] for _ in range(n + 1)]


        for i in range(n):
            name = input()
            if name not in city_map:
                city_map[name] = i + 1

            p = int(input())
            for _ in range(p):
                lines = list(map(int, input().split()))
                graph[i + 1].append(Node(lines[0], lines[1]))

        r = int(input())
        for _ in range(r):
            start_end = input().split()
            start = city_map[start_end[0]]
            end = city_map[start_end[1]]

            dist = [INF for _ in range(n + 1)]
            pq = []

            solution = Solution()
            result = solution.the_shortest_path(start, end)
            print(result)

        input()