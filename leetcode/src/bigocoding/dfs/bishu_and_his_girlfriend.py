class Solution:
    def bishu_and_his_girlfriends(self, N, graph, girlPos):
        visited = [False for _ in range(N + 1)]
        path = (N + 1) * [-1]
        start = 1
        s = []
        s.append(start)
        visited[start] = True
        minDistance = float('inf')
        step = 0
        choice = float('inf')

        while len(s) > 0:
            u = s.pop()
            if u in girlPos:
                if path[u] <= minDistance:
                    minDistance = min(minDistance, path[u])
                    choice = min(u, choice)

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    s.append(v)
                    step += 1
                    path[v] = path[u] + 1

        return choice

'''
Dạng cây thì số đỉnh = số cạnh - 1
E = V - 1
'''


if __name__ == '__main__':

    N = int(input())
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        k = list(map(int, input().split()))
        u, v = k[0], k[1]
        graph[u].append(v)
        graph[v].append(u)

    Q = int(input())
    girlPos = []
    for _ in range(Q):
        girlPos.append(int(input()))

    solution = Solution()
    result = solution.bishu_and_his_girlfriends(N, graph, girlPos)
    print(result)



