class Solution:
    def fasion_in_berland(self, n, nums):
        if n == 1:
            if nums[0] == 1:
                return True
            return False

        total = sum(nums)
    
        if n - total == 1:
            return True
        else:
            return False

class Solution2:
    def fasion_in_berland(self, n, nums):
        from collections import Counter

        if n == 1:
            if nums[0] == 1:
                return True
            return False

        counter = Counter(nums)

        if counter[1] == n: return False
        if counter[0] == 1: return True
        return False


n = int(input())

nums = []
string = input()
arr_str = string.split(' ')
for i in arr_str:
    nums.append(int(i))


solution = Solution2()
result = solution.fasion_in_berland(n, nums)
if result:
    print('YES')
else:
    print('NO')
