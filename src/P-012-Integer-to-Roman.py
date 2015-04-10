class Solution:
    # @return a string
    def intToRoman(self, num):
        ps, ss, re = 'IXCM', 'VLD', ''
        ns = [int(c) for c in str(num)]
        k = len(ns)
        for n in ns:
            k -= 1
            if n == 0:
                pass
            elif n <= 3:
                re += ps[k] * n
            elif n <= 5:
                re += ps[k] * (5 - n) + ss[k]
            elif n <= 8:
                re += ss[k] + ps[k] * (n - 5)
            else:
                re += ps[k] * (10 - n) + ps[k + 1]
        return re

s = Solution()
print s.intToRoman(8)