class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret = 0
        s = 1
        while n >= 2 ** s:
            s += 1
        while n > 0:
            s -= 1
            if n - 2 ** s >= 0:
                ret += 1
                n -= 2 ** s
        return ret

s = Solution()
n = 8
print s.hammingWeight(n)
print bin(n).count('1')