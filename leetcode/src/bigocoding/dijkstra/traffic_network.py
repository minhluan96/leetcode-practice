import heapq


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


class Solution:
    def dijkstra(self, start, dist, graph):
        pq = []
        heapq.heappush(pq, Node(start, 0))
        dist[start] = 0

        while len(pq):
            top = heapq.heappop(pq)
            u = top.id
            w = top.dist
            if dist[u] != w:
                continue

            for neigh in graph[u]:

                if w + neigh.dist < dist[neigh.id]:
                    dist[neigh.id] = w + neigh.dist
                    heapq.heappush(pq, Node(neigh.id, dist[neigh.id]))

    def traffic_network(self, start, end):

        distFromStart = [INF for _ in range(n + 1)]
        self.dijkstra(start, distFromStart, graphStart)

        distFromEnd = [INF for _ in range(n + 1)]
        self.dijkstra(end, distFromEnd, graphEnd)

        ans = distFromStart[end]

        for u in range(len(twoWayGraph)):
            i, j, d = twoWayGraph[u]
            '''
            Since it is a two way routes so we have to calculate both entrances
            '''
            fromStart = distFromStart[i] + d + distFromEnd[j]
            fromEnd = distFromStart[j] + d + distFromEnd[i]
            if fromStart > 0:
                ans = min(ans, fromStart)

            if fromEnd > 0:
                ans = min(ans, fromEnd)

        if ans != INF:
            return ans

        return -1



if __name__ == '__main__':
    s = int(input())
    INF = int(1e9)

    for _ in range(s):
        n, m, k, s, t = list(map(int, input().split()))

        graphStart = [[] for _ in range(n + 1)]
        graphEnd = [[] for _ in range(n + 1)]

        for _ in range(m):
            i, j, d = list(map(int, input().split()))
            graphStart[i].append(Node(j, d))
            '''
            Need to create a reverse map for the end point
            instead using the start graph because it will cause the two way
            section and the dijkstra might calculate the wrong shortest path for
            the start value.
            
            Why do we need it?
            Because we will using it as a bridge to determine the route
            from the start to the point where it has two ways connection and to the end value
            s -> i -> j -> t
            We cannot use the distStart to calculate the distance from j to t
            because it won't reflect the exactly value since we didn't start from j
            We want to calculate the route from j to t. That route j -> t will have the result in
            reverse of the route from t -> j. That's why we need to have a different graph
            '''
            graphEnd[j].append(Node(i, d))

        twoWayGraph = []
        for _ in range(k):
            i, j, d = list(map(int, input().split()))
            twoWayGraph.append([i, j, d])

        solution = Solution()
        result = solution.traffic_network(s, t)
        print(result)

