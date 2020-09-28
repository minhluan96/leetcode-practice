class Solution:
    def findMin(self, nums) -> int:
        '''
            Brute force O(n)
        '''

        min_num = nums[0]

        for n in nums:
            if n < min_num:
                min_num = n

        return min_num

class Solution2:
    def findMin(self, nums) -> int:
        '''
        Using binary search O(logN)
        '''

        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        '''
            if the last element is greater than the first element then there is no rotation.
            ex: 1, 2, 3, 4, 5
        '''
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + int((right - left) / 2)

            '''
                the inflection happened
                if the mid element is greater than its next element then mid+1 element is the smalles
            '''
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            '''
            if the mid element is lesser than its previous element then mid element is the smallest
            '''
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            '''
            if the mid elements value is greater than the 0th element this means
            the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]


            if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            '''
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1



tc = [3,4,5,1,2]

tc = [4,5,1,2,3]
solution = Solution2()
result = solution.findMin(tc)
print(result)