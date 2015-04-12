'''
P-039 - Combination Sum

Given a set of candidate numbers (C) and a target number (T), find all
unique combinations inCwhere the candidate numbers sums toT.
Thesamerepeated number may be chosen fromCunlimited number of times.
Note:All numbers (including target) will be positive integers.Elements
in a combination (a1,a2,  ,ak) must be in non-descending order.
(ie,a1a2  ak).The solution set must not contain duplicate
combinations. For example, given candidate set2,3,6,7and target7,A
solution set is:[7][2, 2, 3]

Tags: Array, Backtracking
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def search(self, target, l = [], start = 0):
        ret = []
        for i in range(start, len(self.c)):
            num = self.c[i]
            if num < target:
                ret += self.search(target - num, l[:] + [num, ], i)
            if num == target:
                ret.append(l[:] + [num, ])
            if num > target:
                break
        return ret

    def combinationSum(self, candidates, target):
        self.c = sorted(candidates)
        return filter(lambda x: len(x) > 0, self.search(target))

s = Solution()
for item in s.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310):
    print item