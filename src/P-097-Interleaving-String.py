'''
P-097 - Interleaving String

Givens1,s2,s3, find whethers3is formed by the interleaving ofs1ands2.
For example,Given:s1="aabcc",s2="dbbca", Whens3="aadbbcbcac", return
true.Whens3="aadbbbaccc", return false.

Tags: Dynamic Programming, String
'''

class Solution:
    # @return a boolean

    # DP-based Solution
    # d[i][j] represents if s3[:i+j] is an interleave of s1[:i] and s2[:j]
    # O(nm) time O(nm) space
    # Space can be optimized to O(n)
    def isInterleave(self, s1, s2, s3):
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        d = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    d[i][j] = True
                elif i == 0:
                    d[i][j] = (s2[:j] == s3[:j])
                elif j == 0:
                    d[i][j] = (s1[:i] == s3[:i])
                else:
                    d[i][j] |= d[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    d[i][j] |= d[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        return d[n][m]

    # BFS-based Solution exists
    # O(nm) time

s = Solution()

s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc"

s1, s2, s3 = "", "b", "b"
s1, s2, s3 = "b", "", "bb"


print s.isInterleave(s1, s2, s3)