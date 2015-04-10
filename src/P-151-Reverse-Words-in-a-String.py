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