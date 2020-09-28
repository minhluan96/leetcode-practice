import queue


class Solution:
    def bfs(self, N, M, catMaps, graph):
        visited = (N + 1) * [False]
        start = 1
        q = queue.Queue()
        visited[start] = True
        q.put(start)
        possibleWays = 0

        if catMaps[start - 1] == 1:
            cats[start] = 1

        while not q.empty():
            u = q.get()

            for n in graph[u]:
                if not visited[n]:
                    visited[n] = True

                    if catMaps[n - 1] == 1:
                        cats[n] = cats[u] + 1

                    if cats[n] <= M:
                        if len(graph[n]) == 1:
                            possibleWays += 1
                        else:
                            q.put(n)

        return possibleWays

    def kefa_and_park(self, N, M, catMaps, graph):
        path = self.bfs(N, M, catMaps, graph)
        return path


if __name__ == '__main__':
    firstLine = list(map(int, input().split()))
    N = firstLine[0]
    M = firstLine[1]

    catMaps = list(map(int, input().split()))

    graph = [[] for i in range(N + 1)]
    cats = [0 for i in range(N + 1)]
    for i in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    solution = Solution()
    result = solution.kefa_and_park(N, M, catMaps, graph)
    print(result)
