class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        evens = []
        odds = []

        for i in range(len(A)):

            if i % 2 == 0:
                odds.append(A[i])
            else:
                evens.append(A[i])

        sumEvens = sum(evens)
        sumOdds = sum(odds)

        counter = 0
        x, y = 0, 0

        for i in range(len(A)):
            if i % 2 == 0:
                sumOdds -= A[i]
            else:
                sumEvens -= A[i]

            if sumOdds + x == sumEvens + y:
                counter += 1

            if i % 2 == 0:
                y += A[i]
            else:
                x += A[i]

        return counter

    def solve2(self, A):
        '''
        Using prefixSum and suffixSum
        '''
        n = len(A)
        odd = 0
        even = 0
        leftOdd = [0] * n
        rightOdd = [0] * n
        leftEven = [0] * n
        rightEven = [0] * n

        for i in range(n):
            leftOdd[i] = odd
            leftEven[i] = even

            if i % 2 == 0:
                even += A[i]
            else:
                odd += A[i]

        odd = 0
        even = 0

        for i in range(n - 1, -1, -1):
            rightOdd[i] = odd
            rightEven[i] = even

            if i % 2 == 0:
                even += A[i]
            else:
                odd += A[i]

        counter = 0
        for i in range(n):
            if leftOdd[i] + rightEven[i] == rightOdd[i] + leftEven[i]:
                counter += 1

        return counter



if __name__ == '__main__':
    A = [2, 1, 6, 4]
    solution = Solution()
    result = solution.solve2(A)
    print(result)