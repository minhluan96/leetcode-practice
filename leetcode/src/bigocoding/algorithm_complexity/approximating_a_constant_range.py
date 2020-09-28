class NaiveSolution:
    '''
    Ok, but not optimal O(N^2)
    ~> wrong sliding window
    '''
    def approximatingAConstantRange(self, n, nums):
        windowStart = 0
        maxLength = 0

        for windowEnd in range(n):
            if windowEnd != windowStart:
                if abs(max(nums[windowStart:windowEnd + 1]) - min(nums[windowStart:windowEnd + 1])) > 1:
                    windowStart += 1

                maxLength = max(windowEnd - windowStart + 1, maxLength)

        return maxLength

'''
lợi dụng |a1 - a1+1| <= 1 
~> tìm mảng có tối đa 2 giá trị phân biệt, sẽ đảm bảo đc điều kiện
sliding window
Time complexity O(2N) ~ O(N)
Space complexity O(N)
'''
class Solution:
    def approximatingAConstantRange(self, n, nums):
        windowStart = 0
        maxLength = 0
        numFrequency = {}

        for windowEnd in range(n):
            numRight = nums[windowEnd]

            if numRight not in numFrequency:
                numFrequency[numRight] = 0
            numFrequency[numRight] += 1
            
            while len(numFrequency) > 2:
                numLeft = nums[windowStart]

                if numLeft in numFrequency:
                    numFrequency[numLeft] -= 1
                if numFrequency[numLeft] == 0:
                    del numFrequency[numLeft]

                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength
                


# n = int(input())
# nums = list(map(int, input().split()))


n = 5
nums = [1,2,3,3,2]

# n = 11
# nums = [5,4,5,5,6,7,8,8,8,7,6]

# n = 20
# nums = [98888,98888,98889,98889,98889,98889,98889,98889,98889,98889,98890,98890,98890,98890,98890,98890,98890,98890,98890,98890]



solution = Solution()
result = solution.approximatingAConstantRange(n, nums)
print(result)



            

