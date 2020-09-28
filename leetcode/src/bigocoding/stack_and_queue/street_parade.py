class Solution:
    '''
    Time complexity: O(N log N) ~> the sort, the rest is O(2N)
    
    there is a way to check the yes or no by checking the stack is empty or not (1), could reduce the time complexity down to O(N)
    
    '''
    def streetParade(self, n, nums):
        stack = []
        results = []
        sortedNums = sorted(nums)

        expect = 1

        for i in range(n):
            if expect == nums[i]:
                results.append(nums[i])
                expect += 1
            else:
                while len(stack) != 0 and stack[-1] == expect:
                    results.append(stack.pop())
                    expect += 1
                
                stack.append(nums[i])
        
        '''
        Get remaining in stack

        (1) could use the expect == nums[i] to check, if satisfied, we push the value into the stack
        '''
        for i in range(len(stack)):
            results.append(stack.pop())

        return sortedNums == results


while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))

    solution = Solution()
    result = solution.streetParade(n, nums)
    if result:
        print('yes')
    else:
        print('no')


# n = 5
# nums = [5,1,2,4,3] 
# solution = Solution()
# result = solution.streetParade(n, nums)
# if result:
#     print('yes')
# else:
#     print('no')
