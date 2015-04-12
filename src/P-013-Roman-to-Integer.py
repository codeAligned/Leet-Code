'''
P-013 - Roman to Integer

Given a roman numeral, convert it to an integer. Input is guaranteed
to be within the range from 1 to 3999.

Tags: Math, String
'''

class Solution:
    # @return a string
    def romanToInt(self, s):
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        k, n = 0, 0
        for i in range(len(s)):
            if i < len(s) - 1 and num[s[i]] < num[s[i + 1]]:
                k += 1
            elif k != 0:
                n += num[s[i]] - num[s[i - 1]] * k
                k = 0
            else:
                n += num[s[i]]
        return n

# Testing
from utils import *

cases = [
	Test_case(('III', ), 3),
	Test_case(('VIII', ), 8),
    Test_case(('XIV', ), 14),
    Test_case(('XVIII', ), 18),
    Test_case(('MMXV', ), 2015),
    Test_case(('MMCDXVII', ), 2417),
]

run_cases(Solution().romanToInt, cases)
