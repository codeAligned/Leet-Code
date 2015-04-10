class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def plus(self, num1, num2):
        (l, s) = (num1, num2) if len(num1) > len(num2) else (num2, num1)
        carry = 0
        ret = ''
        for index in xrange(1, len(s) + 1):
            t = int(s[-index]) + int(l[-index]) + carry
            ret = str(t % 10) + ret
            carry = t / 10
        for index in xrange(len(s) + 1, len(l) + 1):
            t = int(l[-index]) + carry
            ret = str(t % 10) + ret
            carry = t / 10
        if carry:
            ret = str(carry) + ret
        return ret

    def multiply(self, num1, num2):
        ret = ''
        for k, m in enumerate(reversed(num1)):
            carry = 0
            a = '0' * k
            for n in reversed(num2):
                t = int(n) * int(m) + carry
                a = str(t % 10) + a
                carry = t / 10
            if carry:
                a = str(carry) + a
            ret = self.plus(ret, a)
        for k in range(len(ret)):
            if ret[k] != '0':
                break
        return ret[k:]

s = Solution()

n1 = "123789"
n2 = "2"

print s.multiply(n1, n2)
