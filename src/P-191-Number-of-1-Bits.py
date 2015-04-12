'''
P-191 - Number of 1 Bits

Write a function that takes an unsigned integer and returns the number
of 1' bits it has (also known as theHamming weight). For example, the
32-bit integer 11' has binary
representation00000000000000000000000000001011, so the function should
return 3. Credits:Special thanks to@tsfor adding this problem and
creating all test cases.

Tags: Bit Manipulation
'''

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