class Solution:
    '''
    Fast and slow pointers
    '''
    def moveZeroes(self, nums):
        fast, slow = 0, 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            if nums[slow] != 0: 
                slow += 1
            
            fast += 1

        return nums

nums = [1, 0]
solution = Solution()
result = solution.moveZeroes(nums)
print(result)