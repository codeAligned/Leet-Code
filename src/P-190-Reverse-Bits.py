'''
P-190 - Reverse Bits

Reverse bits of a given 32 bits unsigned integer. For example, given
input 43261596 (represented in binary
as00000010100101000001111010011100), return 964176192 (represented in
binary as00111001011110000010100101000000). Follow up:If this function
is called many times, how would you optimize it? Related
problem:Reverse Integer Credits:Special thanks to@tsfor adding this
problem and creating all test cases.

Tags: Bit Manipulation
'''

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