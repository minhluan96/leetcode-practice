import queue


class Solution:
    def bfs(self, start, W, H, maps):
        x = 0
        y = 1
        direction = 4
        direction_x = [0, 0, 1, -1]
        direction_y = [1, -1, 0, 0]

        visited = [[False for _ in range(W)] for _ in range(H)]
        visited[start[x]][start[y]] = True
        q = queue.Queue()
        q.put(start)
        counter = 1

        while not q.empty():
            u = q.get()

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = direction_x[i] + u[x]
                pair[y] = direction_y[i] + u[y]

                if (pair[x] >= 0 and pair[x] < H and pair[y] >= 0 and pair[y] < W) and \
                        maps[pair[x]][pair[y]] == '.' and not visited[pair[x]][pair[y]]:
                    visited[pair[x]][pair[y]] = True
                    counter += 1
                    q.put(pair)

        return counter

    def guilty_prince(self, W, H, maps):
        start = []

        for i in range(H):
            for j in range(W):
                if maps[i][j] == '@':
                    start.append(i)
                    start.append(j)

        counter = self.bfs(start, W, H, maps)

        return counter


if __name__ == '__main__':

    # W = 7
    # H = 7
    # maps = []
    # for i in range(H):
    #     maps.append(list(input()))
    #
    # solution = Solution()
    # result = solution.guilty_prince(W, H, maps)
    # print(result)

    T = int(input())
    for t in range(T):
        wh = list(map(int, input().split()))
        W = wh[0]
        H = wh[1]
        maps = []
        for i in range(H):
            maps.append(list(input()))

        solution = Solution()
        result = solution.guilty_prince(W, H, maps)
        print('Case {}: {}'.format(t + 1, result))
