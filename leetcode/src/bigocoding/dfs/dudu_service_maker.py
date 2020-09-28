import sys

sys.setrecursionlimit(100000000)

class Solution:
    def __init__(self, N, graph):
        self.found = False
        self.visited = [0 for _ in range(N + 1)]
        self.circles = [False for _ in range(N + 1)]
        self.graph = graph

    '''
    0: chua di
    1: di roi - nam tren duog di
    2: di roi - ko nam tren duong di
    '''
    def recursion(self, start):
        self.visited[start] = 1

        for v in self.graph[start]:
            if self.visited[v] == 0:
                self.found = self.recursion(v)
                if self.found:
                    return True
            else:
                if self.visited[v] == 1:
                    return True

        self.visited[start] = 2
        return False

    #
    # def dfs(self, start):
    #     s = []
    #     s.append(start)
    #     self.visited[start] = True
    #     self.circles[start] = True
    #
    #     while len(s) > 0:
    #         u = s.pop()
    #
    #         for v in self.graph[u]:
    #             if self.circles[v]:
    #                 self.found = True
    #                 return
    #
    #             if not self.visited[v]:
    #                 self.circles[v] = True
    #                 self.visited[v] = True
    #                 s.append(v)

    def dudu_service_maker(self, N):
        for i in range(1, N + 1):
            if self.visited[i] == 0:
                self.found = self.recursion(i)
                if self.found:
                    break

        return self.found


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))

        graph = [[] for _ in range(N + 1)]

        for _ in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)

        solution = Solution(N, graph)
        result = solution.dudu_service_maker(N)
        if result:
            print('YES')
        else:
            print('NO')

