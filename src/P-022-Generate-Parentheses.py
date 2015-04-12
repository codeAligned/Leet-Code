'''
P-022 - Generate Parentheses

Givennpairs of parentheses, write a function to generate all
combinations of well-formed parentheses. For example, givenn= 3, a
solution set is: "((()))", "(()())", "(())()", "()(())", "()()()"

Tags: Backtracking, String
'''

class Solution:
    # @param an integer
    # @return a list of string

    # Set-based solution
    # Use set to avoid duplicates
    def generateParenthesis(self, n):
        m = {'()'} if n else {}
        for i in range(n - 1):
            m = {s[:k] + '()' + s[k:] for s in m for k in range(len(s) + 1)}
        return list(m)

    # DP-based solution 
    def generateParenthesis2(self, n):
        m = [[''] for k in range(n + 1)]
        for i in range(1, n + 1):
            # for various length of left part and right part
            m[i] = ['(' + l + ')' + r for j in range(i) for l in m[j] for r in m[i - j - 1]]
        return m[n]

    # Recursive solution
    def generateParenthesis3(self, n):
        ret = []
        self.aux(ret, '', n, 0)
        return ret

    def aux(self, l, s, n, m):
        if not n and not m:
            l.append(s)
        if m > 0:
            self.aux(l, s + ')', n, m - 1)
        if n > 0:
            self.aux(l, s + '(', n - 1, m + 1)


s = Solution()

from time import time
k = 12

t = time()
print len(s.generateParenthesis(k))
print time() - t

t = time()
print len(s.generateParenthesis2(k))
print time() - t

t = time()
print len(s.generateParenthesis3(k))
print time() - t