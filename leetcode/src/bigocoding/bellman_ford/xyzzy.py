class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Solution:
    def bellman_ford(self, start):
        dist[start] = 0

        for i in range(1, N):
            for j in range(len(graph)):
                u = graph[j].source
                v = graph[j].target
                w = graph[j].weight

                if (dist[u] != INF) and (dist[u] + w < dist[v]):
                    dist[v] = dist[u] + w
                    path[v] = u

        for i in range(len(graph)):
            u = graph[i].source
            v = graph[i].target
            w = graph[i].weight
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                return False

        return True

    def xyzzy(self):
        start = 1
        end = N
        playerEnergy = 100

        res = self.bellman_ford(start)
        if not res:
            print('winnable')
        else:
            print('hopeless')

'''

Độ phức tạp O(n^2 + m * (m * n))

Idea

S = 1
N = 1

Bellman ford(S)
Nếu dist[D] > 0:
    print(winnable)
Ngc lại:
    Nếu tồn tại chu trình dương và từ chu trình dương đó có đường đi tới N:
        Sử dụng DFS
        print(winnable)

print(hopeless)

Đọc N
energy = [] // mức năng lượng phòng i
graph = [] // danh sách cạnh
INF = -INF 

Lặp i: 0 > n - 1:
    Đọc e, m
    energy.append(e)
    Lặp j: 0 đến m - 1:
    đọc a
    graph.append(i + 1, a)

Ý tưởng là quy về bài toán tìm đường cho năng lượng lớn nhất

Bellman(S, des) (so sánh lớn hơn do theo ý tưởng)
    dist[s] = 100
    Trong bellman:
    Lặp (u, v) trong graph
    Nếu dist[u] != INF vaf dist[u] + energy[v] > dist[v]:
        DFS(u, d) // O(n * m) do lặp qua từng cạnh trong graph, nếu muốn O(m +n) thì tạo 1 mảng danh sách cạnh kề
        return True (có chu trình dương)
    
    Return True if dist[D] > 0
    
DFS(s, d):
    visited[s] = True
    stack.push(s)
    
    while stack not empty:
        u = stack.top
        Lặp (e, vv) trong graph
            Nếu e == u:
                v = vv
                Nếu !visited[v]:
                ....
            
    
'''


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == -1:
            break
        INF = int(1e9)
        graph = []
        dist = [INF for _ in range(N + 1)]
        path = [-1 for _ in range(N + 1)]


        for k in range(N):
            lines = list(map(int, input().split()))
            weight = lines[0]
            source = k + 1
            doorwaysIndx = 1
            doorways = lines[doorwaysIndx]
            for doorIdx in range(doorways):
                graph.append(Edge(source, lines[doorIdx + doorwaysIndx + 1], weight))

        solution = Solution()
        solution.xyzzy()