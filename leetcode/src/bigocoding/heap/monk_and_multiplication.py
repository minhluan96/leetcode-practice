import queue

class Solution:

    def monk_and_multiplication(self, N, arr):

        result = []
        pq = queue.PriorityQueue()

        for i in range(N):
            if i < 3:
                pq.put(arr[i])
            else:
                if arr[i] > pq.queue[0]:
                    pq.get()
                    pq.put(arr[i])

            if len(pq.queue) < 3:
                result.append(-1)
            else:
                result.append(pq.queue[0] * pq.queue[1] * pq.queue[2])

        return result


if __name__ == '__main__':
    N = int(input())

    arr = list(map(int, input().split()))
    solution = Solution()
    result = solution.monk_and_multiplication(N, arr)
    for i in range(N):
        print(result[i])
