'''
P-067 - Add Binary

Given two binary strings, return their sum (also a binary string). For
example,a ="11"b ="1"Return"100".

Tags: Math, String
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
    	(l, s) = (a, b) if len(a) > len(b) else (b, a)
    	i, c = 0, 0
    	ret = ''
    	for i in range(1, len(s) + 1):
    		t = int(l[-i]) + int(s[-i]) + c
    		ret = str(t % 2) + ret
    		c = t / 2
    	for i in range(len(s) + 1, len(l) + 1):
    		t = int(l[-i]) + c
    		ret = str(t % 2) + ret
    		c = t / 2
    	if c:
    		ret = str(c) + ret
    	return ret

s = Solution()

print s.addBinary('0000001', '1010101')