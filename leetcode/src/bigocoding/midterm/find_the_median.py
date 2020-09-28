import heapq

class Solution:
    def find_the_median(self):
        if len(max_h) == len(min_h):
            return -max_h[0] / 2 + min_h[0] / 2
        return -max_h[0]

if __name__ == '__main__':
    n = int(input())
    min_h = []
    max_h = []

    arr = list(map(int, input().split()))

    for k in arr:
        if not max_h or -max_h[0] >= k:
            heapq.heappush(max_h, -k)
        else:
            heapq.heappush(min_h, k)

        if len(max_h) > len(min_h) + 1:
            heapq.heappush(min_h, -heapq.heappop(max_h))
        elif len(max_h) < len(min_h):
            heapq.heappush(max_h, -heapq.heappop(min_h))


    solution = Solution()
    result = solution.find_the_median()
    print(result)