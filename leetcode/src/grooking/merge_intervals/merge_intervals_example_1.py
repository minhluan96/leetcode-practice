'''
Problem 1: Given a set of intervals, find out if any two intervals overlap.

Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap

Time complexity O(N * logN)
    - O(N): since we have to iterating through the intervals
    - O(NlogN): because we have to sort

Space complexity: O(N) - because we also need a new list for sorting

'''

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def formatIntervals(self, nums):
        return [Interval(x[0], x[1]) for x in nums]

    def isIntervalsOverlap(self, nums):
        if len(nums) < 2: 
            return False
        
        intervals = self.formatIntervals(nums)

        intervals.sort(key=lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:
                return True
            else:
                start = interval.start
                end = interval.end
        
        return False
            
nums = [[1,4], [2,5], [7,9]]
solution = Solution()
result = solution.isIntervalsOverlap(nums)
print(result)


        