class Solution:
    def floyd_warshall(self):
        for i in range(MAX_HOURS):
            for j in range(MAX_HOURS):
                dist[i][j] = graph[i][j]

        for k in range(MAX_HOURS):
            for i in range(MAX_HOURS):
                for j in range(MAX_HOURS):
                    '''
                    i <= k <= j to make sure that we only count those events that didn't overlap
                    '''
                    if dist[i][j] < dist[i][k] + dist[k][j] and i <= k <= j:
                        dist[i][j] = dist[i][k] + dist[k][j]

    def event_organizer(self):
        self.floyd_warshall()
        '''
        Why dist[0][48] is the max compensation?
        Since events should not overlap, all the remaining events lie on the segment [0, S], 
        so the maximal possible compensation for them is maxC[S] by definition of this number. 
        Hence, the total compensation in this case is maxC[S] + C[S][E]. 
        Clearly, in order to get maxC[E], we should get the maximum of maxC[S] + C[S][E] over all S < E. 
        So we arrive at the required formula for maxC[S][E].
        '''
        print(dist[0][48])


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        MAX_HOURS = 49
        graph = [[0 for _ in range(MAX_HOURS)] for _ in range(MAX_HOURS)]
        dist = [[0 for _ in range(MAX_HOURS)] for _ in range(MAX_HOURS)]

        for i in range(N):
            s, d, c = map(int, input().split())
            graph[s][d] = max(graph[s][d], c)

        solution = Solution()
        solution.event_organizer()
