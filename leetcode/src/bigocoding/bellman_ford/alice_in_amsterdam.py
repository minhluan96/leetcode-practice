class Solution:
    def bellman_ford(self, start):
        dist = [INF for _ in range(N)]
        dist[start] = 0
        for i in range(1, N):
            for j in range(len(graph)):
                u = graph[j][0]
                v = graph[j][1]
                w = graph[j][2]

                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w


        '''
            Xem đỉnh nào nằm trong chu trình âm
            
            Những đường đi nào chạy lớn hơn N - 1 lần thì chắc chắn nó nằm trong chu trình âm
            
            INF phải lớn hơn 2^30 * 99 do (K[j] có giá trị lớn nhất là 2^30 và số đỉnh max = 100 )
        '''
        for i in range(1, N):
            for j in range(len(graph)):
                u = graph[j][0]
                v = graph[j][1]
                w = graph[j][2]

                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = -INF

        return dist

    def alice_in_amsterdam(self, start, des):
        if dist2x[start][des] == -INF:
            print('NEGATIVE CYCLE')
        elif dist2x[start][des] == INF:
            print('{}-{} NOT REACHABLE'.format(names[start], names[des]))
        else:
            print('{}-{} {}'.format(names[start], names[des], dist2x[start][des]))


if __name__ == '__main__':

    counter = 1
    while True:
        N = int(input())

        if N == 0:
            break

        print('Case #{}:'.format(counter))
        counter += 1

        INF = int(2**30 * 99 + 1)
        graph = []
        dist2x = []
        names = []

        for x in range(N):
            lines = list(input().split())
            distances = lines[1:]
            names.append(lines[0])
            for y in range(len(distances)):
                distance = int(distances[y])

                if x == y and distance > 0:
                    distance = 0

                if x != y and distance == 0:
                    continue

                graph.append((x, y, distance))


        solution = Solution()

        for s in range(N):
            dist2x.append(solution.bellman_ford(s))


        Q = int(input())

        queries = []

        for _ in range(Q):
            start, end = list(map(int, input().split()))
            solution.alice_in_amsterdam(start, end)



