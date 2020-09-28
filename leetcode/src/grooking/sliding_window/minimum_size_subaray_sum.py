class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        windowStart = 0
        minLength = 0
        totalSum = 0

        for windowEnd in range(len(nums)):
            totalSum += nums[windowEnd]

            while totalSum >= s:
                if minLength == 0 or windowEnd - windowStart + 1 < minLength:
                    minLength = windowEnd - windowStart + 1

                totalSum -= nums[windowStart]
                windowStart += 1

        return minLength
    
nums = [2,3,1,2,4,3]
s = 7
solution = Solution()
result = solution.minSubArrayLen(s, nums)
print(result)