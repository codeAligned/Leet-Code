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