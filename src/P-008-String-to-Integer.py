'''
P-008 - String to Integer (atoi)

Implement atoi to convert a string to an integer.

The function first discards as many whitespace
characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial
plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value. The string can contain
additional characters after those that form the integral number, which
are ignored and have no effect on the behavior of this function. If
the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is
empty or it contains only whitespace characters, no conversion is
performed. If no valid conversion could be performed, a zero value is
returned. If the correct value is out of the range of representable
values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Tags: Math, String
'''

class Solution:
    # @return an integer
    # Spoiler:
    # - Discard the leading zeros or whitespaces
    # - Interpret as many digits as possible
    # - Discard any trailing characters
    # - Return 0 if input not valid
    # - Deal with overflow
    def atoi(self, str):
        limit = 2 ** 31
        n = 0
        negative = False
        starting = True
        for c in str:
            if starting:
                if c == '+':
                    starting = False
                    continue
                if c == '-':
                    starting = False
                    negative = True
                    continue
                if c == '0' or c == ' ' :
                    continue
            if ord(c) <= ord('9') and ord(c) >= ord('0'):
                n = n * 10 + int(c)
                starting = False
            else:
                break
        n = -n if negative else n
        if n >= limit:
            n = limit - 1
        if n < -limit:
            n = -limit
        return n

# Testing
from utils import *

cases = [
    Test_case(('abc', ), '0'),
	Test_case(('123', ), '123'),
    Test_case(('1230', ), '1230'),
    Test_case(('-123', ), '-123'),
    Test_case(('0123', ), '123'),
    Test_case(('+123', ), '123'),
    Test_case(('-0123', ), '-123'),
    Test_case((' 123', ), '123'),
    Test_case(('- 0123', ), '0'),
    Test_case(('123.45', ), '123'),
    Test_case(('9991234567890', ), '2147483647'),
    Test_case(('-9991234567890', ), '-2147483648'),
]

run_cases(Solution().atoi, cases)
