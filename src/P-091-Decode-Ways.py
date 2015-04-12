'''
P-091 - Decode Ways

A message containing letters fromA-Zis being encoded to numbers using
the following mapping: Given an encoded message containing digits,
determine the total number of ways to decode it. For example,Given
encoded message"12",  it could be decoded as"AB"(1 2) or"L"(12). The
number of ways decoding"12"is 2.

Tags: Dynamic Programming, String
'''

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s: 
            return 0
        m = [0] * len(s)
        for i in range(len(s)):
            # check if s[i] itself can be decoded
            if s[i] > '0':
                m[i] += m[i - 1] if i > 0 else 1
            # check if s[i] and s[i - 1] can be decoded together
            if i > 0:
                n = int(s[i - 1] + s[i])
                if s[i - 1] != '0' and n > 0 and n < 27:
                    m[i] += m[i - 2] if i > 1 else 1
        return m[-1]

    # A more concise DP solution
    def numDecodings(self, s):
        if not s:
            return 0
        chars = set([str(i) for i in range(1, 27)])
        m = [0] * (len(s) + 1)
        m[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1 : i] in chars:
                m[i] += m[i - 1]
            if i > 1 and s[i - 2 : i] in chars:
                m[i] += m[i - 2]
        return m[-1]

s = Solution()

print s.numDecodings(''), 0
print s.numDecodings('0'), 0
print s.numDecodings('1'), 1
print s.numDecodings('00'), 0
print s.numDecodings('000'), 0
print s.numDecodings('01'), 0
print s.numDecodings('001'), 0
print s.numDecodings('10'), 1
print s.numDecodings('100'), 0
print s.numDecodings('12'), 2
print s.numDecodings('27'), 1
print s.numDecodings('301'), 0
print s.numDecodings('121'), 3