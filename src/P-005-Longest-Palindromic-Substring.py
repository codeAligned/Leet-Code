'''
P-005 - Longest Palindromic Substring

Given a stringS, find the longest palindromic substring in S. You may
assume that the maximum length of S is 1000, and there exists one unique
longest palindromic substring.

Tags: String
'''

class Solution:
    # @return a string

    # Straightforward
    # O(n ^ 2)
    def is_palindrome(self, start, end, s):
        for i in xrange((end - start + 1) / 2):
            if s[start + i] != s[end - i]:
                return False
        return True

    def longestPalindrome(self, s):
        ms = ml = 0
        for k in range(len(s)):
            # Odd length
            if self.is_palindrome(k - ml, k, s):
                ms = k - ml
                ml += 1
            # Even length
            elif k - ml - 1 >= 0 and self.is_palindrome(k - ml - 1, k, s):
                ms = k - ml - 1
                ml += 2
        return s[ms : ms + ml]

    # Manacher's Algorithm
    # O(n) Time
    def preProcess(self, s):
        if len(s) == 0:
            return "^$"
        ret = "^"
        for c in s:
            ret += '#' + c
        ret += "#$"
        return ret

    def longestPalindrome(self, s):
        T = self.preProcess(s)
        P = [0] * len(T)
        C, R = 0, 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * C - i
            P[i] = min(R - i, P[i_mirror]) if (R > i) else 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        length = max(P)
        index = P.index(length)

        return s[(index - 1 - length)/2 : (index - 1 + length)/2]

# Testing
from utils import *

cases = [
	Test_case(('', ), ''),
    Test_case(('1', ), '1'),
    Test_case(('11', ), '11'),
    Test_case(('131', ), '131'),
    Test_case(('123215', ), '12321'),
    Test_case(('41441', ), '1441'),
    Test_case(('12343252311325', ), '52311325'),
]

run_cases(Solution().longestPalindrome, cases)
