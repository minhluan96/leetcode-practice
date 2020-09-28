class Solution:
    def floyd_warshall(self):
        for i in range(n):
            for j in range(n):
                dist[i][j] = graph[i][j]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    '''
                    The purpose is to find the longest path therefore can maximize the value of exchange
                    '''
                    if dist[i][j] < dist[i][k] * dist[k][j]:
                        dist[i][j] = dist[i][k] * dist[k][j]

    def arbitrage(self):
        self.floyd_warshall()

        after_exchanged = dist[start][start]

        if after_exchanged > 1:
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    counter = 1
    while True:
        n = int(input())

        if n == 0:
            break

        INF = int(1e9)

        graph = [[0 for i in range(n)] for j in range(n)]
        names = [None for i in range(n)]
        dist = [[None for i in range(n)] for j in range(n)]

        nameMap = {}

        for i in range(n):
            names[i] = input()
            nameMap[names[i]] = i

        m = int(input())

        start = -1

        for j in range(m):
            lines = list(input().split())
            s, d = lines[0], lines[2]
            distance = float(lines[1])
            if j == 0:
                start = nameMap[s]

            graph[nameMap[s]][nameMap[d]] = distance

        solution = Solution()
        ans = solution.arbitrage()
        print('Case {}: {}'.format(counter, ans))
        counter += 1

        input()



