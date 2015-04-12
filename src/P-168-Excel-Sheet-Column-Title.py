'''
P-168 - Excel Sheet Column Title

Given a positive integer, return its corresponding column title as
appear in an Excel sheet. For example: Credits:Special thanks
to@ifanchufor adding this problem and creating all test cases.

Tags: Math
'''

class Solution:
    # @return a string
    def convertToTitle(self, num):
        chars = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while num > 0:
            result.insert(0, chars[(num - 1) % 26])
            num = (num - 1) / 26
        return ''.join(result)

s = Solution()
print s.convertToTitle(28)