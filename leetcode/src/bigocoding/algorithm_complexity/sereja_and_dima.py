class Solution:
    def serajaAndDima(self, n, nums):
        left, right = 0, n - 1
        
        count = 0
        totalSeraja, totalDima = 0, 0

        while left < right:
            maxNum = max(nums[left], nums[right])
            
            if count % 2 == 0:
                totalSeraja += maxNum
            else:
                totalDima += maxNum

            if nums[left] < nums[right]:
                right -= 1
            else:
                left += 1

            count += 1

        '''
        leftover
        '''
        if count % 2 == 0:
            totalSeraja += nums[left]
        else:
            totalDima += nums[left]

        return [totalSeraja, totalDima]

n = 4
nums = [4,1,2,10]

# n = 7
# nums = [1,2,3,4,5,6,7]

n = int(input())
nums = list(map(int, input().split()))

solution = Solution()
result = solution.serajaAndDima(n, nums)
print('{} {}'.format(result[0], result[1]))