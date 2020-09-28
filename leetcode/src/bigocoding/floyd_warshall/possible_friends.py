class Solution:
    def floyd_warshall(self):
        i, j = 0, 0
        for i in range(V):
            for j in range(V):
                dist[i][j] = graph[i][j]

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if not dist[i][j] and graph[i][k] and graph[k][j]:
                        possible[i] += 1
                        dist[i][j] = True


    def possible_friends(self):
        self.floyd_warshall()
        maxPerson = (-1, -1)

        for i in range(V):
            if possible[i] > maxPerson[1]:
                maxPerson = (i, possible[i])

        print('{} {}'.format(maxPerson[0], maxPerson[1]))


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        lines = input()

        V = len(lines)

        graph = [[None for i in range(V)] for j in range(V)]
        dist = [[None for i in range(V)] for j in range(V)]
        path = [[None for i in range(V)] for j in range(V)]

        possible = [0 for i in range(V)]

        INF = int(1e9)

        for i in range(V):
            for j in range(V):
                graph[i][j] = False if lines[j] == 'N' and i != j else True

            if i != V - 1:
                lines = input()

        solution = Solution()
        solution.possible_friends()
