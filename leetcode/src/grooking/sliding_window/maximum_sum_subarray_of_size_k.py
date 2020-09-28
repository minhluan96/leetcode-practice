'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

'''
Time complexity O(n * k)
Space complexity O(1)
'''
class NaiveSolution:
    def maximum_sum_subarray_of_size_k(self, arr, k):
        maxSum = 0
        for i in range(len(arr) - k + 1):
            total = 0
            for j in range(i, i + k):
                total += arr[j]
            
            maxSum = max(total, maxSum)
        
        return maxSum


'''
Time complexity O(n)
Space complexity O(1)
'''
class Solution:
    def maximum_sum_subarray_of_size_k(self, arr, k):
        windowStart = 0
        windowSum = 0
        maxSum = 0

        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]

            if windowEnd >= k - 1:
                maxSum = max(windowSum, maxSum)

                windowSum -= arr[windowStart]
                windowStart += 1
        
        return maxSum
    

arr = [2, 3, 4, 1, 5]
k = 2
solution = Solution()
result = solution.maximum_sum_subarray_of_size_k(arr, k)
print(result)