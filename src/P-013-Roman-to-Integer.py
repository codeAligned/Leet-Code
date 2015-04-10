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

    def romanToInt(self, s):
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        k, n = 0, 0
        for i in range(len(s)):
            if i < len(s) - 1 and num[s[i]] < num[s[i + 1]]:
                k += 1
            elif k != 0:
                n += num[s[i]] - num[s[i - 1]] * k
                k = 0
            else:
                n += num[s[i]]
        return n

s = Solution()
for i in range(1, 4000):
    if s.romanToInt(s.intToRoman(i)) != i:
        print i, s.intToRoman(i), s.romanToInt(s.intToRoman(i))