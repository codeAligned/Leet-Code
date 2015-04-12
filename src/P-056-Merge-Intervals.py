'''
P-056 - Merge Intervals

Given a collection of intervals, merge all overlapping intervals. For
example,Given[1,3],[2,6],[8,10],[15,18],return[1,6],[8,10],[15,18].

Tags: Array, Sort
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
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

s = Solution()
l = [
    Interval(1, 2),
    Interval(2, 3),
    Interval(3, 6),
    Interval(8, 10),
    Interval(15, 18)
]
for item in s.merge(l):
    print item.start, item.end