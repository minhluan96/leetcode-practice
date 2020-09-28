class WaterArea:
    def __init__(self, startX, startY, totalArea):
        self.startX = startX
        self.startY = startY
        self.total = totalArea


class Solution:
    def is_rear(self, pair):
        x = 0
        y = 1
        return pair[x] == 0 or pair[x] == N - 1 or pair[y] == 0 or pair[y] == M - 1

    def dfs(self, start, maps, visited):
        x = 0
        y = 1
        direction = 4
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        s = []
        counter = 0
        s.append(start)
        visited[start[x]][start[y]] = True
        isNearOcean = False

        if self.is_rear(start):
            isNearOcean = True

        counter += 1

        while len(s) > 0:
            u = s.pop()
            if counter == -1:
                break

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = dx[i] + u[x]
                pair[y] = dy[i] + u[y]

                if (pair[x] >= 0 and pair[x] < N and pair[y] >= 0 and pair[y] < M) and \
                     maps[pair[x]][pair[y]] == '.':

                    if self.is_rear(pair):
                        isNearOcean = True

                    if not visited[pair[x]][pair[y]]:
                        counter += 1
                        visited[pair[x]][pair[y]] = True
                        s.append(pair)

        return [counter, isNearOcean]

    def dfs_cover_map(self, start, maps, visited):
        x = 0
        y = 1
        direction = 4
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        s = []
        s.append(start)
        visited[start[x]][start[y]] = True
        maps[start[x]][start[y]] = '*'

        while len(s) > 0:
            u = s.pop()

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = dx[i] + u[x]
                pair[y] = dy[i] + u[y]

                if (pair[x] >= 0 and pair[x] < N and pair[y] >= 0 and pair[y] < M) and \
                        not visited[pair[x]][pair[y]] and maps[pair[x]][pair[y]] == '.':
                    maps[pair[x]][pair[y]] = '*'
                    visited[pair[x]][pair[y]] = True
                    s.append(pair)

    def lakes_in_berland(self, n, m, k, maps):
        visited = [[False for _ in range(m)] for _ in range(n)]
        totalArea = []

        for i in range(0, n):
            for j in range(0, m):
                if maps[i][j] == '.' and not visited[i][j]:
                    distance, isNearOcean = self.dfs([i, j], maps, visited)
                    if not isNearOcean:
                        totalArea.append(WaterArea(i, j, distance))

        if len(totalArea) == k:
            return [0, maps]

        totalArea.sort(key=lambda x: x.total)
        acceptArea = []

        leftoverLake = len(totalArea)
        for i in range(len(totalArea)):
            waterArea = totalArea[i]
            if leftoverLake > k:
                acceptArea.append(waterArea)
                leftoverLake -= 1

        visited = [[False for _ in range(m)] for _ in range(n)]
        totalCell = 0
        for i in range(len(acceptArea)):
            waterArea = acceptArea[i]
            totalCell += waterArea.total
            self.dfs_cover_map([waterArea.startX, waterArea.startY], maps, visited)

        return [totalCell, maps]


if __name__ == '__main__':
    nmk = list(map(int, input().split()))
    N = nmk[0]
    M = nmk[1]
    k = nmk[2]

    lines = []
    for _ in range(N):
        lines.append(list(input()))

    solution = Solution()
    result = solution.lakes_in_berland(N, M, k, lines)
    total = result[0]
    maps = result[1]
    print(total)
    for i in range(N):
        for j in range(M):
            print(maps[i][j], end='')
        print()

