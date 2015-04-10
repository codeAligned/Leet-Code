class Solution:
    # @return a boolean

    # Recursive Solution
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        # check every position where the left and right can be swapped
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

    # DP-based Solution
    # dp[i][j][l] means whether s2.substr(j,l) 
    # is a scrambled string of s1.substr(i,l) or not
    # O(n ^ 4) time complexity
    def isScramble(self, s1, s2):
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n + 1)] for __ in range(n + 1)]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                dp[i][j][1] = (s1[i] == s2[j])
                l = 2
                while i + l <= n and j + l <= n:
                    for k in range(1, l):
                        dp[i][j][l] |= dp[i][j][k] and dp[i+k][j+k][l-k]
                        dp[i][j][l] |= dp[i][j+l-k][k] and dp[i+k][j][l-k]
                    l += 1
        return dp[0][0][n]