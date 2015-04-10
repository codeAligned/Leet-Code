class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    # DP-based Solution #1
    # d[i] is whether s[:i + 1] can be break into words in dict
    # In the inner loop, we check every substring
    def wordBreak(self, s, dict):
        d = [False] * len(s)
        d[0] = s[:1] in dict
        for i in range(1, len(s)):
            d[i] = s[:i + 1] in dict
            for j in range(i):
                d[i] |= d[j] and s[j + 1: i + 1] in dict
        return d[-1]

    # DP-based Solution #2
    # d[i] is whether s[:i + 1] can be break into words in dict
    # In the inner loop, we check every word in the dict
    def wordBreak(self, s, dict):
        d = [False] * len(s)
        #d[0] = s[:1] in dict
        for i in range(len(s)):
            for word in dict:
                n = len(word)
                if n <= i + 1:
                    d[i] |= word == s[i - n + 1 : i + 1] and (i + 1 == n or d[i - n])
        return d[-1]

    # BFS-based Solution
    # if there is match in the dict for s[i:j] then there is a path 
    # from i to j + 1

s = Solution()
S = "leetcode"
D = ["leet", "code"]
S = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
D = set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
S = 'abcde'
D = set(['a','b','c','d','e','ab','cd', 'bc', 'de'])

print s.wordBreak(S, D)