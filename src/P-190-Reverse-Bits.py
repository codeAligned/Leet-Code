class Solution:
    # @param n, an integer
    # @return an integer    
    def reverseBits(self, n):
        s = bin(n)[:1:-1]
        s += '0' * (32 - len(s))
        ret = 0
        for i in range(1, 33):
            ret += int(s[-i]) * (2 ** (i - 1))
        return ret

s = Solution()
print s.reverseBits(1)