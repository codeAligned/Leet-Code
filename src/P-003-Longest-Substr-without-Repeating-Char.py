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

s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')
print s.lengthOfLongestSubstring('c')
print s.lengthOfLongestSubstring('cc')
print s.lengthOfLongestSubstring('abcde')