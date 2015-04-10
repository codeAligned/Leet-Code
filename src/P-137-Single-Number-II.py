class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	# use two 32-bit integer to simulate 32 2-bit counter
    	# ones - holds XOR of all the elements appeared "only" once. 
    	# twos - holds XOR of all the elements appeared "only" twice.
		# So if at any point time,
		# A new number appears - It gets XOR'd to the variable "ones".
		# A number gets repeated(appears twice) - 
		# 	It is removed from "ones" and XOR'd to the variable "twos".
		# A number appears for the third time - 
		# 	It gets removed from both "ones" and "twos".
		# https://leetcode.com/discuss/9763/accepted-proper-explaination-does-anyone-have-better-idea
        ones, twos = 0, 0
        for n in A:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones

s = Solution()
from random import random, shuffle
l = range(9) + range(9) + range(9)
shuffle(l)
l.insert(int(random() * 18), 12)

print s.singleNumber(l)
