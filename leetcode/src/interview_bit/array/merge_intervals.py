# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __lt__(self, other):
        return self.start < other.start

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):


        sorted_new_interval = None
        if new_interval.start < new_interval.end:
            sorted_new_interval = new_interval
        else:
            sorted_new_interval = Interval(new_interval.end, new_interval.start)

        intervals.append(sorted_new_interval)

        intervals.sort()

        if len(intervals) < 2:
            return intervals

        merged = []
        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                merged.append(Interval(start, end))
                start = interval.start
                end = interval.end

        merged.append(Interval(start, end))
        return merged


if __name__ == '__main__':
    intervals = [Interval(1, 2), Interval(3, 6)]
    new_interval = Interval(10, 8)
    solution = Solution()
    result = solution.insert(intervals, new_interval)
    print(result)