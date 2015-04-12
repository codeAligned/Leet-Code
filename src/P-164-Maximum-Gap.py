'''
P-164 - Maximum Gap

Given an unsorted array, find the maximum difference between the
successive elements in its sorted form. Try to solve it in linear
time/space. Return 0 if the array contains less than 2 elements. You
may assume all elements in the array are non-negative integers and fit
in the 32-bit signed integer range. Credits:Special thanks
to@porker2008for adding this problem and creating all test cases.

Tags: Sort
'''

from math import ceil
from sys import maxint

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        num = set(num)
        if len(num) < 2:
            return 0
        n_max, n_min = max(num), min(num)
        bsize = (n_max - n_min - 1) / (len(num) - 1) + 1
        bin_max = [0] * (len(num) - 1)
        bin_min = [maxint] * (len(num) - 1)
        for n in num - {n_max, n_min}:
            idx = (n - n_min) / bsize
            bin_max[idx] = max(bin_max[idx], n)
            bin_min[idx] = min(bin_min[idx], n)
        max_gap = 0
        prev = n_min
        for i in range(len(num) - 1):
            if bin_max[i] == 0 and bin_min[i] == maxint:
                continue
            max_gap = max(max_gap, bin_min[i] - prev)
            prev = bin_max[i]
        max_gap = max(max_gap, n_max - prev)
        return max_gap

s = Solution()
l = [1, 100000]
print s.maximumGap(l)