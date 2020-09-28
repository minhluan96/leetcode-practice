class Solution:
    def removeDuplicates(self, nums) -> int:
        ''' Brute force O(n^2) '''
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
                i -= 1
            i += 1

        return len(nums)

class Solution2:
    def removeDuplicates(self, nums) -> int:
        '''
            Time complexity O(n)
            Two pointers, slow runner and fast runner 
            return the new length and the result will be splitted from 0 to the new length
        '''
        if not len(nums): return 0 
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

tc = [1,1,2]
solution = Solution2()
result = solution.removeDuplicates(tc)
print(result)