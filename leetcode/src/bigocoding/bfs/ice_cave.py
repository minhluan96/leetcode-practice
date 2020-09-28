import queue


class Solution:
    def bfs(self, N, M, start, end, maps):
        q = queue.Queue()
        q.put(start)
        direction = 4
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while not q.empty():
            u = q.get()

            for i in range(direction):
                r = u[0] + dx[i]
                c = u[1] + dy[i]
                pair = [r, c]

                if pair == end and maps[r][c] == 'X':
                    return True

                if r < 0 or r >= N or c < 0 or c >= M:
                    continue

                if maps[r][c] == 'X':
                    continue

                maps[r][c] = 'X'
                q.put(pair)

        return False

    def ice_cave(self, N, M, start, end, maps):
        start[0] -= 1
        start[1] -= 1
        end[0] -= 1
        end[1] -= 1
        return self.bfs(N, M, start, end, maps)

'''
    def psuedocode(self, N, M, start, end, maps):
        if self.bfsFix(start, N, M, end, maps):
            print('YES')
        else:
            print('NO')


    def bfsFix(self, start, N, M, end, maps):
        q = queue.Queue()
        q.put(start)
        direction = 4
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]


        while not q.empty():
            u = q.get()

            for i in range(direction):
                r = u[0] + dx[i]
                c = u[1] + dy[i]
                pair = [r, c]

                if pair == end and maps[r][c] == 'X':
                    return True

                if r < 0 or r >= N or c < 0 or c >= M:
                    continue

                if maps[r][c] == 'X':
                    continue

                maps[r][c] = 'X'
                q.put(pair)

        return False

'''

'''
Time complexity O(M * N)
'''

if __name__ == '__main__':
    mn = list(map(int, input().split()))
    N = mn[0]
    M = mn[1]

    lines = []
    for i in range(N):
        lines.append(list(input()))

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    solution = Solution()
    result = solution.ice_cave(N, M, start, end, lines)
    if result:
        print('YES')
    else:
        print('NO')
