class Solution:
    def sortedSquares(self, A):
        firstPointer = 0
        secondPointer = len(A) - 1
        result = [0] * len(A)

        for i in range(len(A) - 1, -1, -1):
            if abs(A[firstPointer]) < abs(A[secondPointer]):
                result[i] = pow(A[secondPointer], 2)
                secondPointer -= 1
            else:
                result[i] = pow(A[firstPointer], 2)
                firstPointer += 1
        
        return result

A = [-7,-3,2,3,11]
solution = Solution()
result = solution.sortedSquares(A)
print(result)
        