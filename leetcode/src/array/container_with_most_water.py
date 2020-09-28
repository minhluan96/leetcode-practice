class Solution:
    def maxArea(self, height) -> int:
        '''
            Time complexity O(n)
            Space complexity O(1)
        '''
        maximum = 0
        left = 0
        right = len(height) - 1

        while left < right:
            between = right - left

            lower_bar = 0

            if height[left] <= height[right]:
                lower_bar = height[left]
                left += 1
            else:
                lower_bar = height[right]
                right -= 1

            prod = between * lower_bar
            if prod > maximum:
                maximum = prod

        return maximum

height = [1,8,6,2,5,4,8,3,7]
height = [3,9,3,4,7,2,12,6]
solution = Solution()
result = solution.maxArea(height)
print(result)