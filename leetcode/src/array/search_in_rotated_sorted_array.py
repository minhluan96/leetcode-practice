class Solution:
    def search(self, nums, target: int) -> int:
        if not len(nums): return -1
        
        left = 0
        right = len(nums) - 1


        '''
            Find the smallest pivot, this loop will break when left == right
            then the smallest will have the pos is left or right, since they are equal
        '''
        while left < right:
            midpoint = left + int((right - left) / 2)
            '''
                This is where we custom the binary search
                In the sorted array, all the elements to the right always greater than the elements to the left, ie [0,1,2,4,5,6,7]
                But in this example
                [4,5,6,7,0,1,2]
                so the mid element is 7 and it's kinda weird because the mid elemennt is greater than the element in the right is 2
                which mean we would know that the array was rotated to the right and the smallest element in that sub array too
                We will put the left equal midpoint + 1 to narrow down the elements
                Otherwise, we will narrow down the right barrier
            '''
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint

        '''
            We store the smallest element in a variable and restart the value of the left and right to prepare the Binary Search
        '''
        start = left
        left = 0
        right = len(nums) - 1


        '''
            We will determine which sub array we would use to find the target
            if the target was greater than the smallest one and was smaller than number to the right then it would be in the right sub array
            Then we will narrow down by setting up the left barrier
            Otherwise we will set up the right barrier
        '''
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start


        '''
        Regular binary search
        '''
        while left <= right:
            midpoint = left + int((right - left) / 2)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
        
        return -1


nums = [4,5,6,7,0,1,2]
target = 1
solution = Solution()
result = solution.search(nums, target)
print(result)