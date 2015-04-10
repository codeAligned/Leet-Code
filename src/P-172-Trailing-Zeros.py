class Solution:
    # @return an integer
    # All trailing zeros is from the factors 5 * 2
    # In n factorial, the number of factor 2 is always greater than 5
    # So we need to count how many 5 factors in all numbers from 1 to n
    def trailingZeroes(self, n):
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)

s = Solution()
print s.trailingZeroes(10)