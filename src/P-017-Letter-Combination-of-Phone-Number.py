'''
P-017 - Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the
number could represent. A mapping of digit to letters (just like on
the telephone buttons) is given below. Note:Although the above answer
is in lexicographical order, your answer could be in any order you
want.

Tags: Backtracking, String
'''

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits, pos = 0, string = None):
        # Initialize
        if pos == 0:
            self.map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
            self.output = []
            string = []
            digits = [int(c) for c in digits if c not in '01']

        if len(string) == len(digits):
            self.output.append(''.join(string))
            return self.output

        # Recursion
        for c in self.map[digits[pos]]:
            string.append(c)
            self.letterCombinations(digits, pos + 1, string)
            string.pop()

        return self.output

# Testing
from utils import *

cases = [
	Test_case(('123', ), 9),
    Test_case(('234', ), 27),
    Test_case(('1234567890', ), 11664),
]

run_cases(Solution().letterCombinations, cases, lambda x: len(x))
