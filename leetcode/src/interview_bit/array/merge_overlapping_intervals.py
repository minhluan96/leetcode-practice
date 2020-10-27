# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __lt__(self, other):
        return self.start < other.start

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort()
        merged = []
        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                merged.append(Interval(start, end))
                start = interval.start
                end = interval.end

        merged.append(Interval(start, end))
        return merged


if __name__ == '__main__':
    intervals = [Interval(1,3),Interval(2,6), Interval(8,10),Interval(15,18)]
    solution = Solution()
    result = solution.merge(intervals)
    print(result)
