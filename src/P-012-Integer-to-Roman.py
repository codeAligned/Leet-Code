'''
P-012 - Integer to Roman

Given an integer, convert it to a roman numeral. Input is guaranteed
to be within the range from 1 to 3999.

Tags: Math, String
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        ps, ss, re = 'IXCM', 'VLD', ''
        ns = [int(c) for c in str(num)]
        k = len(ns)
        for n in ns:
            k -= 1
            if n == 0:
                pass
            elif n <= 3:
                re += ps[k] * n
            elif n <= 5:
                re += ps[k] * (5 - n) + ss[k]
            elif n <= 8:
                re += ss[k] + ps[k] * (n - 5)
            else:
                re += ps[k] * (10 - n) + ps[k + 1]
        return re

# Testing
from utils import *

cases = [
	Test_case((3, ), 'III'),
	Test_case((8, ), 'VIII'),
    Test_case((14, ), 'XIV'),
    Test_case((18, ), 'XVIII'),
    Test_case((2015, ), 'MMXV'),
    Test_case((2417, ), 'MMCDXVII'),
]

run_cases(Solution().intToRoman, cases)
