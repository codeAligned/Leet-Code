'''
P-050 - Pow(x, n)

Implement pow(x,n).

Tags: Math, Binary Search
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        ret = 1.0
        tmp = x if n > 0 else 1 / x
        for c in reversed(bin(n)):
            if c == '1':
                ret *= tmp
            tmp *= tmp
        return ret

s = Solution()
print s.pow(34.00515, 1)