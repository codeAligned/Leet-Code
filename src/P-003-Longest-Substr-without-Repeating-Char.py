'''
P-003 - Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating
characters. For example, the longest substring without repeating letters for
"abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.

Tags: Hash Table, Two Pointers, String
'''

class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		# hashmap, index, current max length, current start point
		m, i, l, t = {}, 0, 0, 0
		for i, c in enumerate(s):
			if c in m and m[c] >= t:
				t = m[c] + 1
			m[c] = i
			l = max(l, i - t + 1)
		return l

from utils import *

cases = [
	Test_case(('abcabcbb',), 3),
	Test_case(('c', ), 1),
	Test_case(('cc', ), 1),
	Test_case(('abcde', ), 5),
]

run_cases(Solution().lengthOfLongestSubstring, cases)
