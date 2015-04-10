class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        ret = []
        carry = 1
        for n in reversed(digits):
            t = n + carry
            carry = t / 10
            ret.insert(0, t % 10)
        if carry:
            ret.insert(0, carry)
        return ret