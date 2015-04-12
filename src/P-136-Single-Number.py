'''
P-136 - Single Number

Given an array of integers, every element appearstwiceexcept for one.
Find that single one. Note:Your algorithm should have a linear runtime
complexity. Could you implement it without using extra memory?

Tags: Hash Table, Bit Manipulation
'''

class Solution:
    # @param A, a list of integer
    # @return an integer

    # XOR all the numbers and two same number will cancel 
    # and leave only the single number
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A, 0)

from random import random, shuffle

length = 9
single = 1

s = Solution()
l = range(1,length) + range(1,length)
shuffle(l)
l.insert(int(random() * 18), single)

print s.singleNumber(l)
