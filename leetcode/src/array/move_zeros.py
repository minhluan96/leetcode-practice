class Solution:
    def moveZeroes(self, nums) -> None:
        ''' Using another array '''
        arr = [n for n in nums if n != 0]
        missing = len(nums) - len(arr)
        arr.extend([0] * missing)
        nums[:] = list(arr)

        return arr


class Solution2:
    def moveZeroes(self, nums) -> None:
        ''' Using two pointers '''
        lastNonZeroFoundAt = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1


        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
        
        return nums

tc = [0,0,0,3,12]
[3, 0, 0, 0, 12]
[3, 12, 0, 0, 0]

#     0 1 2 3  4
# tc = [0,1,0,3,12]
    #[1,0,0,3,12]
    #[1,0,3,0,12]
    #[1,3,0,0,12]
    #[1,3,0,12,0]
    #[1,3,12,0,0]

solution = Solution2()
result = solution.moveZeroes(tc)
print(result)
            