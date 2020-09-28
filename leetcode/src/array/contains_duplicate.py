class Solution:
    def containsDuplicate(self, nums) -> bool:
        nset = set(nums)
        return len(nset) != len(nums)


tc = [1,2,3,4]
solution = Solution()
result = solution.containsDuplicate(tc)
print(result)
        