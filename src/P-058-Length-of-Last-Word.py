'''
P-058 - Length of Last Word

Given a stringsconsists of upper/lower-case alphabets and empty space
characters' ', return the length of last word in the string. If the
last word does not exist, return 0. Note:A word is defined as a
character sequence consists of non-space characters only. For
example,Givens="Hello World",return5.

Tags: String
'''

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        l, i = 0, 0
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                break
        for c in s[:i + 1]:
            l = 0 if c == ' ' else l + 1
        return l

s = Solution()

test = ['', ' ', 'aaa', ' aaa', 'aaa ', 'aa aaa', 'aa aaa ', ' aa ']
for string in test:
    print s.lengthOfLastWord(string)