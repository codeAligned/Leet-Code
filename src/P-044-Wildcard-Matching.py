'''
P-044 - Wildcard Matching

Implement wildcard pattern matching with support for'?'and'*'.

Tags: Dynamic Programming, Backtracking, Greedy, String
'''

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean

    # DP-based Solution
    # dp[n] means the substring s[:n] if match the pattern i
    # dp[0] means the empty string '' or s[:0] which only match the pattern '*'
    def isMatch(self, s, p):
        s_len = len(s)
        if len(p) - p.count('*') > s_len:
            return False
        dp = [True] + [False] * s_len
        for c in p:
            if c != '*':
                for n in reversed(range(s_len)):
                    dp[n + 1] = dp[n] and (c == s[n] or c == '?')
            else:
                for n in range(s_len):
                    # star matches nothing (dp[n + 1]) or
                    # matches one of more character (dp[n])
                    dp[n + 1] = dp[n] or dp[n + 1]
            dp[0] = dp[0] and c == '*'
        return dp[-1]

    # Backtracking Solution
    def isMatch(self, s, p):
        s_curr = p_curr = 0
        s_star_match = p_star_match = -1
        while s_curr < len(s):
            if p_curr < len(p) and (s[s_curr] == p[p_curr] or p[p_curr] == '?'):
                s_curr += 1
                p_curr += 1
            elif p_curr < len(p) and p[p_curr] == '*':
                # check if * matches nothing in s
                s_star_match = s_curr
                p_star_match = p_curr
                p_curr += 1
            elif p_star_match >= 0:
                # check if * matches one of more char in s
                p_curr = p_star_match + 1
                s_curr = s_star_match = s_star_match + 1
            else:
                return False
        # Get rid of extra tailing stars
        while p_curr < len(p) and p[p_curr] == '*':
            p_curr += 1
             
        return p_curr == len(p)
                 
s = Solution()
print s.isMatch("aa","a"), False
print s.isMatch("aa","aa"), True
print s.isMatch("aaa","aa"), False
print s.isMatch("aa", "*"), True
print s.isMatch("aa", "a*"), True
print s.isMatch("ab", "?*"), True
print s.isMatch("aab", "c*a*b"), False