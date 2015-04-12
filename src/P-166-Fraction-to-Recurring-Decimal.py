'''
P-166 - Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a
fraction, return the fraction in string format. If the fractional part
is repeating, enclose the repeating part in parentheses. For
example,Given numerator = 1, denominator = 2, return "0.5".Given
numerator = 2, denominator = 1, return "2".Given numerator = 2,
denominator = 3, return "0.(6)". Credits:Special thanks
to@Shangrilafor adding this problem and creating all test cases.

Tags: Hash Table, Math
'''

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        m = {}
        n, r = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign, str(n), '.']

        # Simulate the division process
        # The result repeats if we see a duplicate remainder
        while r not in m:
            m[r] = len(result)
            n, r = divmod(r * 10, abs(denominator))
            result.append(str(n))
        result.insert(m[r], '(')
        result.append(')')
        
        # Get rid of the evenly divide case
        return ''.join(result).replace('(0)', '').rstrip('.')

s = Solution()
print s.fractionToDecimal(11, 10)