import queue

class Solution:
    def bfs(self, start, N, graph, path):
        visited = (N + 1) * [False]
        
        q = queue.Queue()

        visited[start] = True
        q.put(start)

        '''
        Always start from start there for the path to itself = 0
        '''
        path[start] = 0

        while not q.empty():
            u = q.get()
           
            for n in graph[u]:
                if not visited[n]:
                    visited[n] = True
                    q.put(n)

                    '''
                    If there is a path to the other node, we increase the counter, in this case, we don't 
                    need to track the previous node
                    '''
                    path[n] = path[u] + 1

    def bfsShortestReach(self, Q, N, M, start, graph):
        path = (N + 1) * [-1]
        self.bfs(start, N, graph, path)
        
        for i in range(len(path)):
            if i == 0:
                continue

            if path[i] == -1:
                print(path[i], end=' ')
            elif path[i] != 0:
                print(path[i] * 6, end=' ')
        


# Q = 2
# N = 4
# M = 2

# Q = 1
# N = 3
# M = 1


Q = int(input())

for _ in range(Q):
    nm = input().split()

    N = int(nm[0])

    M = int(nm[1])
    graph = [[] for i in range(N + 1)]

    for i in range(M):
        u, v = map(int, input().split())
        
        graph[u].append(v)
        graph[v].append(u)

    start = int(input())

    solution = Solution()
    solution.bfsShortestReach(Q, N, M, start, graph)
    print()

        


