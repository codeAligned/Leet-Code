'''
P-047 - Permutations II

Given a collection of numbers that might contain duplicates, return
all possible unique permutations. For example,[1,1,2]have the
following unique permutations:[1,1,2],[1,2,1], and[2,1,1].

Tags: Backtracking
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def _permute(self, num):
        from itertools import permutations 
        return [list(item) for item in list(set(list(permutations(num))))]

    def permuteUnique(self, num):
        if not num:
            return []
        return self.permute(sorted(num))

    def permute(self, num):
        if len(num) == 1:
            return [num]

        ret = []
        for index, elt in enumerate(num):
            if index > 0 and num[index - 1] == elt:
                continue
            ret += [[elt] + p for p in self.permute(num[:index] + num[index + 1:])]
        return ret
        
s = Solution()
l = [1,1,2,2]
for item in s.permuteUnique(l):
    print item
print len(s.permuteUnique(l)), len(s._permute(l))