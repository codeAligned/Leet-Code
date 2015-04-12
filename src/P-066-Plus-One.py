'''
P-066 - Plus One

Given a non-negative number represented as an array of digits, plus
one to the number. The digits are stored such that the most
significant digit is at the head of the list.

Tags: Array, Math
'''

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