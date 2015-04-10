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