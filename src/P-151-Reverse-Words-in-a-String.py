'''
P-151 - Reverse Words in a String

Given an input string, reverse the string word by word. For
example,Given s = "the sky is blue",return "blue is sky the". Update
(2015-02-12):For C programmers: Try to solve itin-placeinO(1) space.
click to show clarification. What constitutes a word?A sequence of
non-space characters constitutes a word.Could the input string contain
leading or trailing spaces?Yes. However, your reversed string should
not contain leading or trailing spaces.How about multiple spaces
between two words?Reduce them to a single space in the reversed
string.

Tags: String
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s[::-1]
        ret = ''
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == ' ':
                i += 1
            m = i
            while i < len(s) and s[i] != ' ':
                i += 1
            n = i
            if m < n:
                ret += s[n - 1 : m - 1 : -1] + ' '
        return ret[:-1]

s = Solution()
string = '  the    sky is blue  '
result = s.reverseWords(string)
print len(result), result