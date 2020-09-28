import queue

class Solution:
    def __init__(self):
        self.totalWolve = 0
        self.totalSheep = 0

    def bfs(self, start):
        x = 0
        y = 1
        direction = 4
        direction_x = [0, 0, 1, -1]
        direction_y = [1, -1, 0, 0]

        visited[start[x]][start[y]] = True
        q = queue.Queue()
        q.put(start)

        sheep = 0
        wolve = 0
        canEscape = False

        if map[start[x]][start[y]] == 'k':
            sheep += 1
        if map[start[x]][start[y]] == 'v':
            wolve += 1

        while not q.empty():
            u = q.get()

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = direction_x[i] + u[x]
                pair[y] = direction_y[i] + u[y]

                '''
                Which mean the (x, y) is on the edge, the plus +1 to x and y will
                be outbounded of the map. We can re-write like this instead of
                checking the pair[x] in range and pair[y] in range
                '''
                if not (pair[x] in range(N) and pair[y] in range(M)):
                    canEscape = True
                    continue

                if (pair[x] >= 0 and pair[x] < N and pair[y] >= 0 and pair[y] < M) and \
                    not visited[pair[x]][pair[y]]:
                    visited[pair[x]][pair[y]] = True
                    if map[pair[x]][pair[y]] == 'k':
                        sheep += 1
                    if map[pair[x]][pair[y]] == 'v':
                        wolve += 1
                    q.put(pair)

        if canEscape:
            self.totalSheep += sheep
            self.totalWolve += wolve
        else:
            if sheep > wolve:
                self.totalSheep += sheep
            else:
                self.totalWolve += wolve

    def sheep(self):
        for i in range(N):
            for j in range(M):
                if map[i][j] != '#':
                    self.bfs([i, j])

        print(*[self.totalSheep, self.totalWolve])

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    map = []

    totalWolve = 0
    totalSheep = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(N):
        map.append(list(input()))

    solution = Solution()
    solution.sheep()
    a = 1