'''
P-040 - Combination Sum II

Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations inCwhere the candidate numbers sums toT.
Each number inCmay only be usedoncein the combination. Note:All
numbers (including target) will be positive integers.Elements in a
combination (a1,a2,  ,ak) must be in non-descending order. (ie,a1a2
ak).The solution set must not contain duplicate combinations. For
example, given candidate set10,1,2,7,6,1,5and target8,A solution set
is:[1, 7][1, 2, 5][2, 6][1, 1, 6]

Tags: Array, Backtracking
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def search(self, target, l = [], i = 0):
        ret = []
        while i < len(self.c):
            num = self.c[i]
            if num < target:
                ret += self.search(target - num, l[:] + [num, ], i + 1)
            if num == target:
                ret.append(l[:] + [num, ])
            if num > target:
                break
            i +=  1
            # Skip the same character to avoid duplicates
            while i < len(self.c) and self.c[i] == num:
                i += 1
        return ret

    def combinationSum2(self, candidates, target):
        self.c = sorted(candidates)
        return self.search(target)

s = Solution()
c = [1,2]
t = 1
t = 2
for item in s.combinationSum2(c, t):
    print item