'''
P-140 - Word Break II

Given a stringsand a dictionary of wordsdict, add spaces insto
construct a sentence where each word is a valid dictionary word.
Return all such possible sentences. For example,
givens="catsanddog",dict=["cat", "cats", "and", "sand", "dog"]. A
solution is["cats and dog", "cat sand dog"].

Tags: Dynamic Programming, Backtracking
'''

from collections import defaultdict

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings

    def gen_string(self, s, i, m):
        ret = []
        if i not in m:
            return [s[:i + 1]]
        for j in m[i]:
            word = s[j + 1: i + 1]
            if j < 0:
                ret.append(word)
            else:
                for item in self.gen_string(s, j, m):
                    ret.append(item + ' ' + word)
        return ret

    def wordBreak(self, s, dict):
        m = defaultdict(set)
        d = [False] * len(s)
        d[0] = s[:1] in dict

        for i in range(1, len(s)):
            if s[:i + 1] in dict:
                d[i] = True
                m[i].add(-1)
            for j in range(i):
                if d[j] and s[j + 1: i + 1] in dict:
                    d[i] = True
                    m[i].add(j)
        if d[-1]:
            return self.gen_string(s, len(s) - 1, m)
        return []

s = Solution()
S = 'abcde'
D = set(['a','b','c','d','e','ab','cd', 'bc', 'de'])

for item in s.wordBreak(S, D):
    print item