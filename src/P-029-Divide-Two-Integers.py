class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        # check for zero divisor
        if divisor == 0:
            raise ZeroDivisionError
        ret, max_int = 0, 2 ** 31 - 1
        positive = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            st = divisor
            sr = 1
            while dividend >= st + st:
                st += st
                sr += sr
            dividend -= st
            ret += sr

        # check for overflow
        if positive and ret > max_int:
            return max_int
        if not positive and ret > max_int + 1:
            return -max_int - 1
        
        return ret if positive else -ret

s = Solution()

a,b = -2147483648, -1
print s.divide(a, b)
        