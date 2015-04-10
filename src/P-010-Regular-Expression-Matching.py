class Solution:
    # @return a boolean

    # DP-based Solution
    # dp[i][j] means if p[:i + 1] matches s[:j + 1]
    def isMatch(self, s, p):
        n, m = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == '*':
                    dp[i][j] = dp[i - 2][j] or dp[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] |= dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
        return dp[-1][-1]

s = Solution()
pattern = ["a", "aa", "aa", "a*", ".*", ".*", "c*a*b", 'ab*a', '.*c', "a*a*a*a*a*a*a*a*a*a*c"]
strings = ["aa", "aa", "aaa", "aa", "aa", "ab", "aab", 'aaa', 'ab', "aaaaaaaaaaaaab"]
import re
for P, S in zip(pattern, strings):
    print s.isMatch(S, P),'\t', re.search('^' + P + '$', S) is not None