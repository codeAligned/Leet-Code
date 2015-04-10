class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer

    # use the function combine(n, k) 
    # which generate all k-length combinations from n
    # and then iterate through all lengthes
    def aux(self, ret, level = 0, s = 0):
        if self.k == level:
            self.ret.append(ret[:])
            return
        for i in range(s, self.n - self.k + level):
            ret.append(self.s[i])
            self.aux(ret, level + 1, i + 1)
            ret.pop()

    def combine(self, n, k):
        self.ret = []
        self.k = k
        self.n = n + 1
        self.aux([])
        return self.ret

    def subsets(self, S):
    	S.sort()
        self.s = S
        ret = []
        for i in range(len(S) + 1):
        	ret += self.combine(len(S), i)
        return ret

s = Solution()
for item in s.subsets([1, 2, 3]):
	print item