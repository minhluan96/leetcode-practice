class Solution:
    def array(self, n, k, nums):
        windowStart = 0
        numFrequency = {}
        segment = []

        for windowEnd in range(n):
            rightNum = nums[windowEnd]

            if rightNum not in numFrequency:
                numFrequency[rightNum] = 0
            numFrequency[rightNum] += 1

            while len(numFrequency) >= k:
                leftNum = nums[windowStart]
                segment = [windowStart + 1, windowEnd + 1]
                
                numFrequency[leftNum] -= 1
                if numFrequency[leftNum] == 0:
                    del numFrequency[leftNum]

                windowStart += 1

        if not len(segment):
            segment = [-1, -1]

        return segment


firstLine = list(map(int, input().split()))
n = firstLine[0]
k = firstLine[1]
nums = list(map(int, input().split()))
solution = Solution()
result = solution.array(n, k, nums)
print('{} {}'.format(result[0], result[1]))