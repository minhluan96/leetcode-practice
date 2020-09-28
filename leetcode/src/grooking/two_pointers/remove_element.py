class Solution:
    def removeElement(self, nums, val: int) -> int:
        firstPointer = 0
        lastPointer = len(nums) - 1

        if val not in nums:
            return len(nums)

        nums.sort()

        while firstPointer < lastPointer:
            if nums[firstPointer] == val and nums[lastPointer] == val:
                break

            if nums[firstPointer] != val:
                firstPointer += 1
            
            if nums[lastPointer] != val:
                lastPointer -= 1

        del nums[firstPointer:lastPointer + 1]
        return len(nums)

nums = [2]
val = 3
solution = Solution()
result = solution.removeElement(nums, val)
print(result)
print(nums)
