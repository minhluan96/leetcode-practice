class Solution:
    def max_consecutive_ones_iii(self, A, K):
        maxLength = 0
        windowStart = 0
        counter = 0

        for windowEnd in range(len(A)):
            rightNumb = A[windowEnd]

            if rightNumb == 0:
                counter += 1
            
            while counter > K:
                leftNumb = A[windowStart]
                
                if leftNumb == 0:
                    counter -= 1

                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength

a = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
solution = Solution()
result = solution.max_consecutive_ones_iii(a, k)
print(result)