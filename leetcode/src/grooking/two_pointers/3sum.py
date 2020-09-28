class Solution:
    '''
        Time complexity O(N^2)
    '''
    def threeSum(self, nums):
        '''
        The key is the array is sorted
        '''
        nums.sort()
        results = []
        
        for target in range(len(nums) - 2):
            '''
            Remove duplicates if nums[target] is the same number with the previous
            '''
            if target > 0 and nums[target] == nums[target - 1]:
                continue
            firstPointer = target + 1
            secondPointer = len(nums) - 1

            while firstPointer < secondPointer:
                total = nums[firstPointer] + nums[secondPointer] + nums[target]

                if total == 0:
                    triplet = [nums[target], nums[firstPointer], nums[secondPointer]]
                    results.append(triplet)
                    '''
                    Remove duplicates if nums[**pointer] is the same number with the previous
                    '''
                    while firstPointer < secondPointer and nums[firstPointer] == nums[firstPointer + 1]:
                        firstPointer += 1
                    while firstPointer < secondPointer and nums[secondPointer] == nums[secondPointer - 1]:
                        secondPointer -= 1

                    firstPointer += 1
                    secondPointer -= 1

                elif total < 0:
                    firstPointer += 1
                else:
                    secondPointer -= 1
            
        return results

nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)
print(result)