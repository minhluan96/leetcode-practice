'''
Chon 1 điểm: ~> Tìm đc 1 trong 2 đỉnh của đường kính, gọi là x
Từ x, tìm đc đỉnh còn lại, gọi là y

Độ phức tạp O(T * (V + E))

Cau truc dạng cây thì sổ cạnh = số đỉnh - 1
'''

class Solution:
    def __init__(self):
        self.distance = []

    def dfs(self, start):
        for i in range(1, N + 1):
            self.distance[i] = -1
            visited[i] = False

        s = []
        s.append(start)
        self.distance[start] = 0

        visited[start] = True

        while len(s) > 0:
            u = s.pop()

            for v, w in graph[u]:
                if not visited[v]:
                    self.distance[v] = self.distance[u] + w
                    s.append(v)
                    visited[v] = True

    def benefactor(self):
        x = 1
        self.dfs(x)
        for i in range(2, N):
            if self.distance[i] > self.distance[x]:
                x = i
        self.dfs(x)

        result = 0
        for i in range(N):
            result = max(result, self.distance[i])

        return result