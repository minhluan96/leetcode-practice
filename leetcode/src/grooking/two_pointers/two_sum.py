class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):
            if target - num in numMap:
                return [numMap[target - num], i]
            else:
                numMap[num] = i
        
        return []

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)
            