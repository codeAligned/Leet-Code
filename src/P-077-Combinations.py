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