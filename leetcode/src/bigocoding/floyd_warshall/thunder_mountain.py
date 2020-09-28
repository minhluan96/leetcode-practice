class Solution:
    def floyd_warshall(self):
        for i in range(M):
            for j in range(M):
                dist[i][j] = graph[i][j]

        for k in range(M):
            for i in range(M):
                for j in range(M):
                    if dist[i][j] < dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    def thunder_mountain(self):
        self.floyd_warshall()
        a = 2


if __name__ == '__main__':
    N = int(input())

    for case in range(N):

        INF = int(1e9)

        M = int(input())

        graph = [[-INF for _ in range(M)] for _ in range(M)]
        dist = [[-INF for _ in range(M)] for _ in range(M)]

        for i in range(M):
            lines = list(map(int, input().split()))
            for j in range(len(lines)):
                graph[i][j] = lines[j]

        solution = Solution()
        solution.thunder_mountain()




