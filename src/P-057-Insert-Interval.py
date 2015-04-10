# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def merge(self, intervals):
        ret = []
        intervals.sort(key = lambda x : x.start)
        for interval in intervals:
            if not ret or interval.start > ret[-1].end:
                ret.append(interval)
            else:
                ret[-1].end = max(ret[-1].end, interval.end)
        return ret

    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])
