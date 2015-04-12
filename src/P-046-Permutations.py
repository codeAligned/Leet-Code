'''
P-046 - Permutations

Given a collection of numbers, return all possible permutations. For
example,[1,2,3]have the following
permutations:[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2], and[3,2,1].

Tags: Backtracking
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def _permute(self, num):
        from itertools import permutations 
        return [list(item) for item in list(set(list(permutations(num))))]

    def aux(self, k):
        if k == len(self.num):
            self.ret.append(self.num[:])
            return

        for i in range(k, len(self.num)):
            self.num[k], self.num[i] = self.num[i], self.num[k]
            self.aux(k + 1)
            self.num[k], self.num[i] = self.num[i], self.num[k]

    def permute(self, num):
        self.num = num
        self.ret = []
        self.aux(0)
        return self.ret
        
s = Solution()
l = range(1,6)
for item in s.permute(l):
    print item
print len(s.permute(l)), len(s._permute(l))