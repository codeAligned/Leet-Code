'''
P-009 - Palindrome Number

Determine whether an integer is a palindrome. Do this without extra
space. click to show spoilers. Could negative integers be palindromes?
(ie, -1) If you are thinking of converting the integer to string, note
the restriction of using extra space. You could also try reversing an
integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you
handle such case? There is a more generic way of solving this problem.

Tags: Math
'''

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x % 10 == 0 and x != 0 or x < 0:
            return False
        i = 0
        while i < x:
            # digit from the beginning
            i = i * 10 + x % 10
            # digit from the end
            x = x / 10
        return i == x or i / 10 == x

# Testing
from utils import *

cases = [
	Test_case((123, ), False),
    Test_case((-123, ), False),
    Test_case((-121, ), False),
    Test_case((12321, ), True),
    Test_case((1221, ), True),
    Test_case((121, ), True),
    Test_case((1, ), True),
]

run_cases(Solution().isPalindrome, cases)
