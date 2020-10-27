class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxVal = max(A)
        minVal = min(A)
        return maxVal + minVal

if __name__ == '__main__':
    A = [-2, 1, -4, 5, 3]
    solution = Solution()
    result = solution.solve(A)
    print(result)