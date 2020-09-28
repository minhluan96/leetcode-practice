class Solution:
    def floyd_warshall(self):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = 1 if graph[i][j] else INF

        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if dist[i][j] > dist[i][k] + dist[k][j] and dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = dist[i][k] + dist[k][j]

    def risk(self, start, end):
        print('{:2d} to {:2d}: {:d}'.format(start, end, dist[start][end]))


if __name__ == '__main__':
    counter = 1
    while True:
        try:
            N = 20

            INF = int(1e9)

            graph = [[False for _ in range(N + 1)] for _ in range(N + 1)]
            dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
            path = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
            possible = [[] for _ in range(N + 1)]

            for i in range(1, N):
                lines = list(map(int, input().split()))
                numbers = lines[0]

                for j in lines[1:]:
                    if j != 0:
                        graph[i][j] = True
                        graph[j][i] = True

            Q = int(input())
            solution = Solution()
            solution.floyd_warshall()

            print('Test Set #{}'.format(counter))
            counter += 1

            for i in range(Q):
                a, b = list(map(int, input().split()))
                solution.risk(a, b)

            print()
        except EOFError:
            break