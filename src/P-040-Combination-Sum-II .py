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