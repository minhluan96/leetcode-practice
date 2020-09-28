class Solution:
    def floyd_warshall(self):
        for i in range(1, C + 1):
            for j in range(1, C + 1):
                dist[i][j] = graph[i][j]
                dist[j][i] = graph[j][i]
                costliest_city[i][j] = max(cost_hosting[i - 1], cost_hosting[j - 1])
                costliest_city[j][i] = max(cost_hosting[i - 1], cost_hosting[j - 1])

        for _ in range(2):
            for k in range(1, C + 1):
                for i in range(1, C + 1):
                    for j in range(1, C + 1):
                        host = max(costliest_city[i][k], costliest_city[k][j])
                        if dist[i][j] + costliest_city[i][j] > dist[i][k] + dist[k][j] + host:
                            dist[i][j] = dist[i][k] + dist[k][j]
                            costliest_city[i][j] = host

    def asterix_and_obelix(self, start, end):
        distance = dist[start][end]
        if distance == INF:
            print(-1)
            return

        print(distance + costliest_city[start][end], flush=True)


if __name__ == '__main__':
    counter = 1

    while True:
        C, R, Q = map(int, input().split())

        if C == 0 and R == 0 and Q == 0:
            break
        if counter != 1:
            print()

        print('Case #{}'.format(counter), flush=True)

        cost_hosting = list(map(int, input().split()))

        INF = int(1e9)
        graph = [[INF for _ in range(C + 1)] for _ in range(C + 1)]
        dist = [[INF for _ in range(C + 1)] for _ in range(C + 1)]
        costliest_city = [[0 for _ in range(C + 1)] for _ in range(C + 1)]

        for _ in range(R):
            s, d, w = map(int, input().split())
            graph[s][d] = w
            graph[d][s] = w

        solution = Solution()
        solution.floyd_warshall()

        for _ in range(Q):
            s, d = map(int, input().split())
            solution.asterix_and_obelix(s, d)

        counter += 1
