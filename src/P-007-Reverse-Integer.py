class Solution:
    # @return an integer
    # Spoiler:
    # - Deal with trailing zeros in the input
    # - Overflow
    def reverse(self, x):
        limit = 2 ** 31
        ret = int(str(abs(x))[::-1])
        if ret > limit:
            return 0
        if x < 0:
            return -ret
        return ret

s = Solution()
print s.reverse(-123)