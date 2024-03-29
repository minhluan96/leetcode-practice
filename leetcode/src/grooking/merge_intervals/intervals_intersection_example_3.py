'''
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Time complexity O(N + M)
Space complexity O(N) if ignore the result list, the space complexity is O(1)
'''

class Solution:
    def intersection(self, intervals_a, intervals_b):
        i, j = 0, 0
        start, end = 0, 1
        result = []

        while i < len(intervals_a) and j < len(intervals_b):
            a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                intervals_a[i][start] <= intervals_b[j][end]

            b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and \
                intervals_b[j][start] <= intervals_a[i][end]

            if a_overlaps_b or b_overlaps_a:
                result.append([max(intervals_a[i][start], intervals_b[j][start]), \
                    min(intervals_a[i][end], intervals_b[j][end])])

            if intervals_a[i][end] < intervals_b[j][end]:
                i += 1
            else:
                j += 1
        
        return result


intervals_a = [[1, 3], [5, 6], [7, 9]]
intervals_b = [[2, 3], [5, 7]]

solution = Solution()
result = solution.intersection(intervals_a, intervals_b)
print(result)
