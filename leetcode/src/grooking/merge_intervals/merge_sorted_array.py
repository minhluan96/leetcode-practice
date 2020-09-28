class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i, j = m - 1, n - 1
        lastPointer = m + n - 1


        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[lastPointer] = nums1[i]
                i -= 1

            else:
                nums1[lastPointer] = nums2[j]
                j -= 1
            
            lastPointer -= 1

        '''
        If the j pointer > 0 which mean the nums2 still have value that haven't run yet. 
        That's mean all the while loop broke because of the i pointer has smaller than 0 and the condition if nums1[i] > nums2[j] keep return True
        which mean all the larger values have placed in the empty space
        All we need now is cover those values in nums2 that haven't run yet
        '''
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        
        return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
solution = Solution()
result = solution.merge(nums1, m, nums2, n)
print(result)