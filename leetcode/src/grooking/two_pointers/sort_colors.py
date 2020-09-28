class NaiveSolution:
    '''
    Time complexity O(N^2)
    '''
    def sortColors(self, nums) -> None:
        for i in range(len(nums)):
            fastPointer = i + 1
            while fastPointer < len(nums):
                if nums[i] > nums[fastPointer]:
                    nums[i], nums[fastPointer] = nums[fastPointer], nums[i]
                fastPointer += 1
        
        return nums


class Solution:
    '''
    Time complexity O(N)
    Explaination: https://leetcode.com/problems/sort-colors/discuss/681526/Python-O(n)-3-pointers-in-place-approach-explained
    The idea here is the following: we keep 3 pointers
    The idea here is to put sorted 0 and 1 to the beginning and sorted 2s to the end.
    Then we iterate over all elements and process each new element in the following way.
    '''
    def sortColors(self, nums) -> None:
        beginPointer, lastPointer = 0, len(nums) - 1
        currentPointer = 0

        while currentPointer <= lastPointer:
            if nums[currentPointer] == 0:
                nums[currentPointer], nums[beginPointer] = nums[beginPointer], nums[currentPointer]
                currentPointer += 1
                beginPointer += 1
                '''
                We know that the currentPointer is faster than the beginPointer and it only does the swapping if the value is 0
                If we meet a 2, it will be pushed to the end
                '''
            elif nums[currentPointer] == 2:
                nums[currentPointer], nums[lastPointer] = nums[lastPointer], nums[currentPointer]
                '''
                Right here, we don't want to increase the currentPointer because we don't know is the value of nums[lastPointer]
                It could be 0, 1 or worst case is 2. If the value is 2, we want to check it again and move it to the end
                '''
                lastPointer -= 1
            else:
                currentPointer += 1
            

nums = [2,0,2,1,1,0]
solution = Solution()
result = solution.sortColors(nums)
print(result)