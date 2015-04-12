'''
P-077 - Combinations

Given two integersnandk, return all possible combinations ofknumbers
out of 1 ...n. For example,Ifn= 4 andk= 2, a solution is:

Tags: Backtracking
'''

class Solution:
    # @return a list of lists of integers

    # Backtracking
    def aux(self, ret, level = 0, s = 0):
        if level == self.k:
            self.ret.append(ret[:])
            return
        for i in range(s, self.n - self.k + level):
            ret.append(i + 1)
            self.aux(ret, level + 1, i + 1)
            ret.pop()

    def combine(self, n, k):
        self.ret = []
        self.k = k
        self.n = n + 1
        self.aux([])
        return self.ret

s = Solution()
for item in s.combine(4, 2):
    print item