import queue

class Solution:
    def dhoom4(self, start, end, N, keys):
        maximum = 100001
        visited = [-1 for i in range(maximum)]
        q = queue.Queue()
        visited[start] = 0
        q.put(start)

        while not q.empty():
            u = q.get()
            if u == end:
                break
                
            for v in range(N):
                prod = u * keys[v]
                prod %= 100000
                if visited[prod] == -1:
                    visited[prod] = visited[u] + 1
                    if prod == end:
                        return visited[prod]

                    q.put(prod)

        return visited[end]


    '''
    Số đỉnh 1000000
    số cạnh N * 1000000
    độ phức tạp O(V + E)
    
    '''
    def fixDhoom4(self, start, end, N, keys):
        q = queue.Queue()
        dist[start] = 0
        q.put(start)

        while not q.empty():
            u = q.get()

            for i in range(N):
                v = u * keys[i] % 100000

                if dist[v] == -1:
                    dist[v] = dist[u] + 1

                    if v == end:
                        return dist[v]

                    q.put(v)

        return dist[end]

    def main(self):
        if self.fixDhoom4() == -1:
            print(-1)
        else:
            print(dist[end])



firstLine = list(map(int, input().split()))
start = firstLine[0]
end = firstLine[1]
N = int(input())
keys = list(map(int, input().split()))
solution = Solution()
result = solution.dhoom4(start, end, N, keys)
print(result)