'''
P-016 - 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum
is closest to a given number, target. Return the sum of the three
integers. You may assume that each input would have exactly one
solution.

Tags: Array, Two Pointers
'''

class Solution:
    # @return the sum of the three integers
    # O(n ^ 2) Solution
    def threeSumClosest(self, num, target):
        num.sort()
        m = target - sum(num[:3])
        for k in range(len(num) - 2):
            i, j = k + 1, len(num) - 1
            while i < j:
                t = target - num[i] - num[j] - num[k]
                m = min(m, t, key = abs)
                if t > 0:
                    i += 1
                elif t < 0:
                    j -= 1
                else:
                    return target
        return target - m

# Testing
from utils import *

cases = [
	Test_case(([0, 0, 0], 1), 0),
    Test_case(([0, 0, 0, 1], 1), 1),
    Test_case(([0, 0, 0, 3, -2], 1), 1),
]

run_cases(Solution().threeSumClosest, cases)
