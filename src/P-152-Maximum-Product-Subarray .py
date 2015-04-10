class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        ret = imax = imin = A[0]
        for n in A[1:]:
            # swap if the multiplier is negative
            if n < 0:
                imax, imin = imin, imax
            imax = max(n, imax * n)
            imin = min(n, imin * n)
            ret = max(ret, imax)
        return ret


s = Solution()
l = [2, 3, -2, 4]
print s.maxProduct(l)