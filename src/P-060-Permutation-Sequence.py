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