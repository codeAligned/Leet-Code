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