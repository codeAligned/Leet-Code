'''
P-171 - Excel Sheet Column Number

Related to questionExcel Sheet Column Title Given a column title as
appear in an Excel sheet, return its corresponding column number. For
example: Credits:Special thanks to@tsfor adding this problem and
creating all test cases.

Tags: Math
'''

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