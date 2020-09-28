class Solution:
    def floyd_warshall(self, graph, dist):
        i, j = 0, 0
        for i in range(ALPHABET_LENGTH):
            graph[i][i] = 0
        for i in range(ALPHABET_LENGTH):
            for j in range(ALPHABET_LENGTH):
                dist[i][j] = graph[i][j]

        for k in range(ALPHABET_LENGTH):
            for i in range(ALPHABET_LENGTH):
                for j in range(ALPHABET_LENGTH):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    def meeting_prof(self):
        self.floyd_warshall(graphY, distY)
        yDirect = distY[yPos]
        self.floyd_warshall(graphM, distM)
        mDirect = distM[mPos]

        minPath = INF
        for i in range(ALPHABET_LENGTH):
            d = yDirect[i] + mDirect[i]
            if d < minPath:
                minPath = d

        if minPath >= INF:
            print('You will never meet.')
            return

        found = False
        same_length = []
        for i in range(ALPHABET_LENGTH):
            d = yDirect[i] + mDirect[i]
            if d == minPath:
                if found:
                    same_length.append(names[i])
                else:
                    found = True
                    same_length.append(names[i])

        same_length.sort()
        print('{}'.format(minPath), end='')
        for s in same_length:
            print(' {}'.format(s), end='')
        print()


if __name__ == '__main__':
    while True:
        N = int(input())

        if N == 0:
            break

        ALPHABET_LENGTH = 26

        INF = int(1e9)
        graphY = [[INF for i in range(ALPHABET_LENGTH)] for j in range(ALPHABET_LENGTH)]
        graphM = [[INF for i in range(ALPHABET_LENGTH)] for j in range(ALPHABET_LENGTH)]
        distY = [[INF for i in range(ALPHABET_LENGTH)] for j in range(ALPHABET_LENGTH)]
        distM = [[INF for i in range(ALPHABET_LENGTH)] for j in range(ALPHABET_LENGTH)]

        names = [None for i in range(ALPHABET_LENGTH)]
        nameMap = {}

        pos = 0

        for i in range(N):
            lines = input().split()
            p_type = lines[0]
            d_type = lines[1]
            s, d = lines[2], lines[3]
            distance = int(lines[4])

            if s not in nameMap:
                nameMap[s] = pos
                names[pos] = s
                pos += 1

            if d not in nameMap:
                nameMap[d] = pos
                names[pos] = d
                pos += 1

            if p_type == 'Y':
                graphY[nameMap[s]][nameMap[d]] = min(distance, graphY[nameMap[s]][nameMap[d]])
                if d_type == 'B':
                    graphY[nameMap[d]][nameMap[s]] = min(distance, graphY[nameMap[d]][nameMap[s]])

            else:
                graphM[nameMap[s]][nameMap[d]] = min(distance, graphM[nameMap[s]][nameMap[d]])
                if d_type == 'B':
                    graphM[nameMap[d]][nameMap[s]] = min(distance, graphM[nameMap[d]][nameMap[s]])

        yStart, mStart = input().split()

        if yStart not in nameMap or mStart not in nameMap:
            if yStart == mStart:
                print('{} {}'.format(0, yStart))
            else:
                print('You will never meet.')
        else:
            yPos = nameMap[yStart]
            mPos = nameMap[mStart]

            solution = Solution()
            solution.meeting_prof()




