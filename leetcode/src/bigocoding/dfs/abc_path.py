class Solution:
    def __init__(self):
        self.counter = 0
        self.maxVal = 0

    def iterative(self, posX, posY):
        s = []
        idx = 1
        s.append([posX, posY])
        visited[posX][posY] = True

        while len(s) > 0:
            u = s.pop()

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = dx[i] + u[x]
                pair[y] = dy[i] + u[y]

                if (pair[x] >= 0 and pair[x] < H and pair[y] >= 0 and pair[y] < W) and \
                        not visited[pair[x]][pair[y]] and lines[pair[x]][pair[y]] == alphabet[idx]:
                    self.counter += 1
                    visited[pair[x]][pair[y]] = True
                    idx += 1

    def dfs(self, posX, posY, idx):
        if idx == len(alphabet) - 1:
            return

        visited[posX][posY] = True

        for i in range(direction):
            nextX = posX + dx[i]
            nextY = posY + dy[i]

            if (nextX >= 0 and nextX < H and nextY >= 0 and nextY < W) and \
                not visited[nextX][nextY] and lines[nextX][nextY] == alphabet[idx + 1]:
                #print(alphabet[idx + 1])
                self.counter += 1
                self.dfs(nextX, nextY, idx + 1)

        visited[posX][posY] = False
        self.maxVal = max(self.maxVal, self.counter)
        self.counter = 1


    def abc_path(self):
        for i in range(H):
            for j in range(W):
                if not visited[i][j] and lines[i][j] == 'A':
                    self.counter += 1
                    self.dfs(i, j, 0)
                    #self.iterative(i, j)
                    #self.maxVal = max(self.counter, self.maxVal)
                    self.counter = 0

        return self.maxVal


if __name__ == '__main__':
    k = 0
    while True:
        k += 1
        HW = list(map(int, input().split()))
        H = HW[0]
        W = HW[1]

        if H == 0 and W == 0:
            break

        direction = 8
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        alphabet = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
        visited = [[False for _ in range(W)] for _ in range(H)]
        x, y = 0, 1


        lines = []
        for _ in range(H):
            lines.append(list(input()))

        solution = Solution()
        result = solution.abc_path()
        print('Case {}: {}'.format(k, result))

