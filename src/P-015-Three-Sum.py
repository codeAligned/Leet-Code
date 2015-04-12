'''
P-015 - 3Sum

Given an array S of n integers, are there elements a,b,c in S such that
a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: Elements in a triplet (a,b,c) must be in non-descending order.
The solution set must not contain duplicate triplets.

Tags: Array, Two Pointers
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    # O(n ^ 2) Solution
    def threeSum(self, num):
        ret = []
        num = sorted(num)
        for k in range(len(num) - 2):
            # get rid of the duplicates - num[k] != num[k - 1]
            if k == 0 or k > 0 and num[k] != num[k - 1]:
                i, j, t = k + 1, len(num) - 1, -num[k]
                while i < j:
                    n = num[i] + num[j]
                    if t > n:
                        i += 1
                    elif t < n:
                        j -= 1
                    else:
                        ret.append([num[k], num[i], num[j]])
                        # get rid of the duplicates - two while loops
                        while i < j and num[i] == num[i + 1]:
                            i += 1
                        while i < j and num[j] == num[j - 1]:
                            j -= 1
                        i += 1
                        j -= 1
        return ret

# Testing
from utils import *

cases = [
	Test_case(([0, 0, 0], ), [[0, 0, 0], ]),
    Test_case(([0, 0, 0, 1], ), [[0, 0, 0], ]),
    Test_case(([0, 0, 0, 1], ), [[0, 0, 0], ]),
    Test_case(([0, 0, 0, 1, -1], ), [[0, 0, 0], [-1, 0, 1]]),
]

run_cases(Solution().threeSum, cases)
