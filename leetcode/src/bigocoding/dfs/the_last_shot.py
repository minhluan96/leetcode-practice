class Solution:
    def dfs(self, start, visited):
        s = []
        s.append(start)
        visited[start] = True
        counter = 1

        while len(s) > 0:
            u = s.pop()

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    s.append(v)
                    counter += 1

        return counter

    def the_last_shot(self):
        maxValue = 0
        for i in range(1, n + 1):
            visited = [False for _ in range(n + 1)]
            numberOfBomb = self.dfs(i, visited)
            maxValue = max(maxValue, numberOfBomb)

        return maxValue


if __name__ == '__main__':
    mn = list(map(int, input().split()))
    n = mn[0]
    m = mn[1]

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        k = list(map(int, input().split()))
        u, v = k[0], k[1]
        graph[u].append(v)

    solution = Solution()
    result = solution.the_last_shot()
    print(result)
