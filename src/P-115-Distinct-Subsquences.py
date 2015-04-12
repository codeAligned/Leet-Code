'''
P-115 - Distinct Subsequences

Given a stringSand a stringT, count the number of distinct
subsequences ofTinS. A subsequence of a string is a new string which
is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the
remaining characters. (ie,"ACE"is a subsequence of"ABCDE"while"AEC"is
not). Here is an example:S="rabbbit",T="rabbit" Return3.

Tags: Dynamic Programming, String
'''

class Solution:
    # @return an integer
    # d[i][j] means the # of subseq if T[j] in S[i]
    def numDistinct(self, S, T):
        n, m = len(S), len(T)
        d = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            # Empty string is a subseq of any seq
            d[i][0] = 1
            # No need to go beyond i + 1 or m + 1
            for j in range(1, min(i + 1, m + 1)):
                if S[i - 1] == T[j - 1]:
                    d[i][j] = d[i - 1][j - 1] + d[i - 1][j]
                else:
                    d[i][j] = d[i - 1][j]
        return d[n][m]

s = Solution()
S = "rabbbit"
T = "rabbit"

print s.numDistinct(S, T)