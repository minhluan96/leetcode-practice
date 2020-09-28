import queue


class Solution:
    def bfs(self, start, N, M, maps, visited):
        x = 0
        y = 1
        direction = 4
        direction_x = [0, 0, 1, -1]
        direction_y = [1, -1, 0, 0]
        counter = 0

        visited[start[x]][start[y]] = True
        q = queue.Queue()
        q.put(start)
        counter += 1

        while not q.empty():
            u = q.get()

            for i in range(direction):
                pair = [-1, -1]
                pair[x] = direction_x[i] + u[x]
                pair[y] = direction_y[i] + u[y]

                if (pair[x] >= 0 and pair[x] < N and pair[y] >= 0 and pair[y] < M) and \
                    maps[pair[x]][pair[y]] == '1' and not visited[pair[x]][pair[y]]:
                    visited[pair[x]][pair[y]] = True
                    counter += 1
                    q.put(pair)

        return counter

    def slick(self, N, M, lines):
        maps = lines
        start = [-1, -1]
        visited = [[False for _ in range(M)] for _ in range(N)]
        slickFrequency = {}
        for i in range(N):
            for j in range(M):
                if maps[i][j] == '1' and not visited[i][j]:
                    start[0] = i
                    start[1] = j
                    counter = self.bfs(start, N, M, maps, visited)
                    if counter not in slickFrequency:
                        slickFrequency[counter] = 0
                    slickFrequency[counter] += 1

        total = sum(slickFrequency.values())
        sortFrequency = dict(sorted(slickFrequency.items()))
        return [total, sortFrequency]


if __name__ == '__main__':
    while True:
        NM = list(map(int, input().split()))
        N = NM[0]
        M = NM[1]
        if N == 0 or M == 0:
            break

        maps = []
        for i in range(N):
            maps.append(list(input().split()))

        solution = Solution()
        result = solution.slick(N, M, maps)
        print(result[0])
        slickFrequency = result[1]
        for k, v in slickFrequency.items():
            print('{} {}'.format(k, v))

