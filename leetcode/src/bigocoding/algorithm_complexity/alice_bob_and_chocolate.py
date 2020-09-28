class Solution:
    def aliceBobAndChocolate(self, n, nums):
        aliceTime = 0
        bobTime = 0

        i, j = 0, n - 1
        counter = 0

        while i < j:
            if aliceTime <= bobTime:
                aliceTime += nums[i]
                counter += 1
                i += 1
            else:
                bobTime += nums[j]
                j -= 1

        if n % 2 == 0:
            if aliceTime <= bobTime:
                counter += 1

        return [counter, n - counter]

n = 5
nums = [2,9,8,2,7]

n = 4
nums = [4,3,2,8]

# n = int(input())
# nums = list(map(int, input().split()))

solution = Solution()
result = solution.aliceBobAndChocolate(n, nums)
print('{} {}'.format(result[0], result[1]))


