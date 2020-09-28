import queue


class Solution:
    def bfs(self, path, M, N, lines):
        x = 0
        y = 1
        direction = 4
        direction_x = [0, 0, 1, -1]
        direction_y = [1, -1, 0, 0]

        visited = [[False for _ in range(N)] for _ in range(M)]
        visited[path[0][x]][path[0][y]] = True
        q = queue.Queue()

        q.put(path[0])

        while not q.empty():
            u = q.get()
            if path[1][x] == u[x] and path[1][y] == u[y]:
                return True

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = direction_x[i] + u[x]
                pair[y] = direction_y[i] + u[y]

                if (pair[x] >= 0 and pair[x] < M and pair[y] >= 0 and pair[y] < N) and \
                        lines[pair[x]][pair[y]] == '.' and not visited[pair[x]][pair[y]]:
                    visited[pair[x]][pair[y]] = True
                    q.put(pair)

        return False

    def validateTheMaze(self, M, N, lines):
        path = []
        validator = [[False for i in range(N)] for i in range(M)]
        counter = 0
        for i in range(N):
            if lines[0][i] == '.' and not validator[0][i]:
                counter += 1
                validator[0][i] = True
                path.append([0, i])

        for i in range(N):
            if lines[M - 1][i] == '.' and not validator[M - 1][i]:
                counter += 1
                validator[M - 1][i] = True
                path.append([M - 1, i])

        for i in range(M):
            if lines[i][0] == '.' and not validator[i][0]:
                counter += 1
                validator[i][0] = True
                path.append([i, 0])

        for i in range(M):
            if lines[i][N - 1] == '.' and not validator[i][N - 1]:
                counter += 1
                validator[i][N - 1] = True
                path.append([i, N - 1])

        if counter != 2:
            return 'invalid'
        if self.bfs(path, M, N, lines):
            return 'valid'

        return 'invalid'

if __name__ == '__main__':

# T = int(input())

# for _ in range(T):
#     mn = list(map(int, input().split()))
#     M = mn[0]
#     N = mn[1]
#     lines = []
#     for i in range(M):
#         lines.append(list(input()))


#     solution = Solution()
#     result = solution.validateTheMaze(M, N, lines)
#     print(result)

    M = 4
    N = 4

    lines = []
    for i in range(M):
        lines.append(list(input()))

    solution = Solution()
    result = solution.validateTheMaze(M, N, lines)
    print(result)
