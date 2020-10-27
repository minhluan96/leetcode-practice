class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        arr = list(A)
        for i in range(1, len(arr)):
            if arr[i - 1] > 0:
                arr[i] += arr[i - 1]

        return max(arr)

    def maxSubArray2(self, A):
        arr = list(A)
        total = 0
        INF = int(1e9)
        maxSum = -INF

        for i in range(len(arr)):
            total += arr[i]
            maxSum = max(maxSum, total)
            if total < 0:
                total = 0

        return maxSum


if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    result = solution.maxSubArray(A)
    print(result)


