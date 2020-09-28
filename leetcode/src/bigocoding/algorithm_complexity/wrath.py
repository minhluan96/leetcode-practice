class Solution:
    def wrath(self, n, nums):
        totalDeath = 0

        '''
        Set the maxLength equal to n instead of the value of n - 1 or n - 1 because
        we use this to count the number of death, the last person won't be killed no matter what
        Therefore, no reason we set it equal to the last person, it will violate the first condition
        and count the last personn
        '''
        killRange = n

        for i in range(n - 1, -1, -1):
            '''
            If the position was in the kill range, the death counter will increase 
            '''
            if i >= killRange:
                totalDeath += 1
            killRange = min(killRange, i - nums[i])

        return n - totalDeath

n = 4
nums = [0,1,0,10]


# n = 2
# nums = [0,0]


# n = 10
# nums = [1,1,3,0,0,0,2,1,0,3]

# n = int(input())
# nums = list(map(int, input().split()))

solution = Solution()
result = solution.wrath(n, nums)
print(result)
            
            

            