class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
            Brute force O(n * k)
        '''
        
        left = k % len(nums) if k > len(nums) else k

        rotate_pos = len(nums) - left
        
        while rotate_pos > 0:
            first_item = nums[0]

            for i in range(len(nums)):
                if i == len(nums) - 1:
                    nums[i] = first_item
                else:
                    nums[i] = nums[i + 1]

            rotate_pos -= 1
        
        return nums



class Solution2:
    def rotate(self, nums, k: int) -> None:
        '''
            Using additional array - O(n)
            space complexity O(n)
        '''

        left = k % len(nums) if k > len(nums) else k
        rotate_pos = len(nums) - left

        right_arr = nums[rotate_pos:]
        left_arr = nums[:rotate_pos]

        for i in range(len(nums)):
            if i < len(right_arr):
                nums[i] = right_arr[i]
            else:
                nums[i] = left_arr[i - len(right_arr)]
        
        return nums


class Solution3:
    '''
        Using reverse, time complexity O(n) , space complexity O(1)
        In this approach, we firstly reverse all the elements of the array. 
        Then, reversing the first k elements followed by reversing the rest n-kn−k elements gives us the required result.
    '''
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        return nums
        



tc = [1,2,3,4,5,6,7]
k = 3
solution = Solution3()
result = solution.rotate(tc, k)
print(result)
