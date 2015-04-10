class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def aux(self, ret, level = 0, s = 0):
        if self.k == level:
            self.ret.add(tuple(ret))
            return
        for i in range(s, self.n - self.k + level):
            ret.append(self.s[i])
            self.aux(ret, level + 1, i + 1)
            ret.pop()

    def combine(self, n, k):
        self.ret = set()
        self.k = k
        self.n = n + 1
        self.aux([])
        return self.ret

    def subsetsWithDup(self, S):
    	S.sort()
        self.s = S
        ret = []
        for i in range(len(S) + 1):
        	ret += self.combine(len(S), i)
        return [list(item) for item in ret]

s = Solution()
for item in s.subsetsWithDup([1, 2, 2]):
	print item