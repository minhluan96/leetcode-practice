'''
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''


'''
Time complexity O(n * k)
Space complexity O(1)
'''
class NaiveSolution:
    def smallest_subarray_with_a_given_sum(self, arr, s):
        smallest = 0

        for i in range(len(arr)):
            total = 0
            for j in range(i, len(arr)):
                total += arr[j]

                if total >= s:
                    lengthSubArr = j - i + 1
                    if smallest == 0 or lengthSubArr < smallest:
                        smallest = lengthSubArr
                    
                    break
        
        return smallest

'''
Time complexity O(N) for the outer for. The inner while loop processes each element only once.
Therefore the total time complexity is O(N + N) = O(N)
Space complexity O(1) 
'''
class Solution:
    def smallest_subarray_with_a_given_sum(self, arr, s):
        windowStart = 0
        windowSum = 0
        minSubLength = 0

        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]

            '''
            shrink the window as small as possible until the 'window_sum' is smaller than 's'
            '''
            while windowSum >= s:
                lengthSubArr = windowEnd - windowStart + 1
                if minSubLength == 0 or lengthSubArr < minSubLength:
                    minSubLength = lengthSubArr

                windowSum -= arr[windowStart]
                windowStart += 1

        return minSubLength


arr = [2, 1, 5, 2, 3, 2]
s = 7
solution = Solution()
result = solution.smallest_subarray_with_a_given_sum(arr, s)
print(result)