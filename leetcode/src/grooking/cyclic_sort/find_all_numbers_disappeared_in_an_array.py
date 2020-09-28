class Solution:
    def findDisappearedNumbers(self, nums):
        if not len(nums): 
            return []

        missing = []
        start = 0
        
        while start < len(nums):
            n = nums[start]
            if n != start + 1 and n != nums[n - 1]:
                nums[start], nums[n - 1] = nums[n - 1], nums[start]
            else:
                start += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                missing.append(i + 1)

        return missing


nums = [4,3,2,7,8,2,3,1]
solution = Solution()
result = solution.findDisappearedNumbers(nums)
print(result)
