class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0

        firstPointer = 0

        for secondPointer in range(1, len(nums)):
            if nums[firstPointer] != nums[secondPointer]:
                firstPointer += 1
                '''
                At the point where nums[firstPointer] != nums[secondPointer],
                if we don't assign, it will has a chance to duplicate since the next element could be the same as the nums[secondPointer]
                ex: 0, 0, 1, 1, 1
                Therefore, this assignment to avoid the duplication
                '''
                nums[firstPointer] = nums[secondPointer]

        return firstPointer + 1

nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)