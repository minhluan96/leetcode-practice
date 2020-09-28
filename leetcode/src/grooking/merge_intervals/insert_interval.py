class Solution:
    def insert(self, intervals, newInterval):
        start, end = 0, 1
        i = 0
        results = []

        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            results.append(intervals[i])
            i += 1


        '''
        Check the new interval overlaps with the interval[i]
        newInterval come first
        '''
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        results.append(newInterval)

        while i < len(intervals):
            results.append(intervals[i])
            i += 1

        return results


intervals = [[1,3],[6,9]]
newInterval = [2,5]
solution = Solution()
result = solution.insert(intervals, newInterval)
print(result)