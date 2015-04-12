'''
P-007 - Reverse Integer

Reverse digits of an integer.

Example 1 : x =  123, return 321
Example 2 : x = -123, return -321

Here are some good questions to ask before coding.
If the integer's last digit is 0, what should the output be?
ie, cases such as 10, 100. Did you notice that
the reversed integer might overflow? Assume the input is a 32-bit
integer, then the reverse of 1000000003 overflows. How should you
handle such cases? For the purpose of this problem, assume that your
function returns 0 when the reversed integer overflows.

Tags: Math
'''

class Solution:
    # @return an integer
    def reverse(self, x):
        limit = 2 ** 31
        ret = int(str(abs(x))[::-1])
        if ret > limit:
            return 0
        if x < 0:
            return -ret
        return ret

# Testing
from utils import *

cases = [
	Test_case((-123, ), -321),
	Test_case((123, ), 321),
    Test_case((1000000003, ), 0),
]

run_cases(Solution().reverse, cases)
