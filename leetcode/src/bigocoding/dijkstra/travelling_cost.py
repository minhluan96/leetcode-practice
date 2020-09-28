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

    def travelling_cost(self, start, end):
        self.dijkstra(start)
        if dist[end] == INF:
            print('NO PATH')
        else:
            print(dist[end])



if __name__ == '__main__':
    N = int(input())
    INF = int(1e9)
    dist = [INF for i in range(501)]
    graph = [[] for i in range(501)]
    pq = []

    node_list = []

    for _ in range(N):
        lines = list(map(int, input().split()))
        i = lines[0]
        j = lines[1]
        d = lines[2]

        node_list.append(i)
        node_list.append(j)
        graph[i].append(Node(j, d))
        graph[j].append(Node(i, d))

    node_list = list(set(node_list))

    U = int(input())
    Q = int(input())

    for _ in range(Q):
        V = int(input())
        solution = Solution()
        solution.travelling_cost(U, V)



