class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        l = len(s)
        ret = 0
        for c in s:
            l -= 1
            ret += (ord(c) - 64) * 26 ** l
        return ret