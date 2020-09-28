class Solution:
    def dfs(self, start, graph, visited):
        s = []
        s.append(start)
        visited[start] = True

        while len(s) > 0:
            u = s.pop()

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    s.append(v)

    def prayatna(self, N, E, graph):
        if E == 0:
            return N

        visited = [False for _ in range(N)]
        counter = 0

        for i in range(N):
            if not visited[i]:
                self.dfs(i, graph, visited)
                counter += 1

        return counter


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        E = int(input())

        graph = [[] for _ in range(N)]

        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        solution = Solution()
        result = solution.prayatna(N, E, graph)
        print(result)

    # N = int(input())
    # E = int(input())
    #
    # graph = [[] for _ in range(N + 1)]
    #
    # for _ in range(E):
    #     u, v = map(int, input().split())
    #     graph[u].append(v)
    #     graph[v].append(u)
    #
    # solution = Solution()
    # result = solution.prayatna(N, E, graph)
    # print(result)
