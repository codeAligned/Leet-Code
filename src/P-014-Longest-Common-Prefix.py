'''
P-014 - Longest Common Prefix

Write a function to find the longest common prefix string amongst an
array of strings.

Tags: String
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) > 1:
                return strs[0][:i]
        return min(strs)

# Testing
from utils import *

cases = [
	Test_case((['abc', 'abd'],), 'ab'),
    Test_case((['abc', 'abc'],), 'abc'),
    Test_case((['abc', ''],), ''),
]

run_cases(Solution().longestCommonPrefix, cases)
