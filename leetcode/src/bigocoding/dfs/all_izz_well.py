class Solution:
    def __init__(self):
        self.isFound = False

    def dfs(self, start, visited):
        s = []
        direction = 8
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        default_s = 'ALLIZZWELL'
        idx = 0
        x = 0
        y = 1

        s.append(start)
        visited[start[x]][start[y]] = True


        while len(s) > 0:
            u = s.pop()

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = dx[i] + u[x]
                pair[y] = dy[i] + u[y]

                if idx == len(default_s) - 1:
                    self.isFound = True
                    visited[pair[x]][pair[y]] = False
                    return True

                if (pair[x] >= 0 and pair[x] < R and pair[y] >= 0 and pair[y] < C) and \
                    not visited[pair[x]][pair[y]] and maps[pair[x]][pair[y]] == default_s[idx + 1]:
                    visited[pair[x]][pair[y]] = True
                    s.append(pair)
                    idx += 1

        return False


    # def recursion_dfs(self, posX, posY, idx):
    #
    #     if idx == 9:
    #         self.isFound = True
    #         return
    #
    #     visited[posX][posY] = True
    #
    #     for i in range(direction):
    #         nextX = posX + dx[i]
    #         nextY = posY + dy[i]
    #
    #         if (nextX >= 0 and nextX < R and nextY >= 0 and nextY < C) and \
    #             not visited[nextX][nextY] and maps[nextX][nextY] == default_s[idx + 1]:
    #             self.recursion_dfs(nextX, nextY, idx + 1)
    #
    #   visited[posX][posY] = False

    def all_izz_well(self):

        for i in range(R):
            for j in range(C):
                if not visited[i][j] and maps[i][j] == 'A':
                    #self.recursion_dfs(i, j, 0)
                    self.isFound = self.dfs([i, j], visited)
                    if self.isFound:
                        return True

        return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        RC = list(map(int, input().split()))
        R = RC[0]
        C = RC[1]

        direction = 8
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        default_s = 'ALLIZZWELL'
        visited = [[False for _ in range(C)] for _ in range(R)]

        x = 0
        y = 1



        maps = []
        for _ in range(R):
            maps.append(list(input()))

        newline = input()

        solution = Solution()
        result = solution.all_izz_well()
        if result:
            print('YES')
        else:
            print('NO')




