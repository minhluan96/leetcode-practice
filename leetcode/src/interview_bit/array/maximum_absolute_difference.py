import math

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        N = len(A)

        ap = [A[i] + i for i in range(N)]
        am = [A[i] - i for i in range(N)]

        return max(max(ap) - min(ap), max(am) - min(am))

if __name__ == '__main__':
    A = [ -98, -5, 37, -97, 38, 22, 70, 42, 61, 84 ]
    solution = Solution()
    result = solution.maxArr(A)
    print(result)
