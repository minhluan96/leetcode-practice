class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        startPos, endPos = 0, 1
        results = []

        intervals.sort(key=lambda x: x[startPos])

        start = intervals[0][startPos]
        end = intervals[0][endPos]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[startPos] <= end:
                end = max(interval[endPos], end)
            else:
                results.append([start, end])
                start = interval[startPos]
                end = interval[endPos]

        results.append([start, end])

        return results

intervals = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
result = solution.merge(intervals)
print(result)
        

        