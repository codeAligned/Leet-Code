'''
P-060 - Permutation Sequence

The set[1,2,3,&#8230;,n]contains a total ofn! unique permutations. By
listing and labeling all of the permutations in order,We get the
following sequence (ie, forn= 3):"123""132""213""231""312""321"
Givennandk, return thekthpermutation sequence. Note:Givennwill be
between 1 and 9 inclusive.

Tags: Backtracking, Math
'''

class Solution:

    def getPermutation(self, n, k):
        f = reduce(lambda x, y: x * y, xrange(1, n + 1), 1)
        k = (k - 1) % f
        ret = ''
        d = [str(i) for i in xrange(1, n + 1)]
        
        while k >= 0 and len(d) > 0:
            f /= n
            n -= 1
            i = k / f
            k -= i * f
            ret += d.pop(i)
        return ret + ''.join(reversed(d))

s = Solution()
for i in range(1, 10):
    print i, s.getPermutation(3, i)