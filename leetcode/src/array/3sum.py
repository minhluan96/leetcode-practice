class Solution:
    def threeSum(self, nums):
        '''
        The main idea is to iterate every number in nums.
        We use the number as a target to find two other numbers which make total zero.
        For those two other numbers, we move pointers, low and high, to try them.

        low start from left to right.
        high start from right to left.
        '''

        '''
        First, we sort the array, so we can easily move i around and know how to adjust low and high.
        The basic idea of moving the low and high pointer to the center is the array has to be sorted
        '''
        nums = sorted(nums)
        output = []

        '''
        we only move the i pointer to the len(nums) - 2 because we have to save the room for two others in the triplet
        Ex: [-1, 0, 1, 2, -1, -4]. And the nums[i] = 2 so it is possible that the next one and the next one of the next one can form to the triplet
        '''
        for i in range(len(nums) - 2):
            '''
            If the number is the same as the number before, we have used it as target already. We won't calculate and skip to the next iteration
            '''
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                '''
                We always start the low pointer from i+1 because the combination of 0~i has already been tried
                Ex: i = 1 has run through all the greater element than it
                so if i = 3, we don't have to re-run the i = 1, 2 again.
                '''
                low = i + 1
                high = len(nums) - 1
                
                '''
                a + b + c = 0 ~> a + b = 0 - c
                '''
                total = 0 - nums[i]

                while low < high:
                    if nums[low] + nums[high] == total:
                        output.append([nums[i], nums[low], nums[high]])


                        '''
                        We need to move the left and right pointers to the next different numbers, so we do not get repeating result. 
                        We don't want to have the duplicate in the result
                        '''
                        while low < high and nums[low] == nums[low + 1]: low += 1
                        while low < high and nums[high] == nums[high - 1]: high -= 1

                        '''
                        Once we go to the right spot, we will increase the low and decrease the high by one
                        '''
                        low += 1
                        high -= 1

                    elif nums[low] + nums[high] > total:
                        '''
                        If the sum of low and high is greater than total, we need it to be smaller, so we move the high pointer.
                        '''
                        high -= 1
                    else:
                        '''
                        If the sum of low and high is smaller than total, we need it to be greater, so we move the low pointer.
                        '''
                        low += 1

        return output




nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)
print(result)