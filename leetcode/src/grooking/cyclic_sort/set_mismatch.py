class Solution:
    def findErrorNums(self, nums):
        start = 0

        while start < len(nums):
            n = nums[start]
            '''
            We want to swap the nums which has the position isn't correct
            Ex: [3,2,2] ~> nums[0] = 3, if correct, the 3 should be placed at pos 2 (nums[0] - 1)
            so we check that place, nums[nums[0] - 1] to see the value is mismatch or not

            It is equal to the nums[start] != start + 1 and nums[start] != nums[nums[start] - 1]
            '''
            if n != nums[n - 1]:
                nums[start], nums[n - 1] = nums[n - 1], nums[start]
            else:
                start += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]

        return []


nums = [1,2,2,4]

nums = [3,2,2]

solution = Solution()
result = solution.findErrorNums(nums)
print(result)