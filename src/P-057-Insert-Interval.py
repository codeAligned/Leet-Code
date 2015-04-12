'''
P-057 - Insert Interval

Given a set ofnon-overlappingintervals, insert a new interval into the
intervals (merge if necessary). You may assume that the intervals were
initially sorted according to their start times. Example 1:Given
intervals[1,3],[6,9], insert and merge[2,5]in as[1,5],[6,9]. Example
2:Given[1,2],[3,5],[6,7],[8,10],[12,16], insert and merge[4,9]in
as[1,2],[3,10],[12,16]. This is because the new interval[4,9]overlaps
with[3,5],[6,7],[8,10].

Tags: Array, Sort
'''

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
