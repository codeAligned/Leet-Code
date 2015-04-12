'''
P-038 - Count and Say

The count-and-say sequence is the sequence of integers beginning as
follows:1, 11, 21, 1211, 111221, ... 1is read off as"one 1"or11.11is
read off as"two 1s"or21.21is read off as"one 2, thenone 1"or1211.
Given an integern, generate thenthsequence. Note: The sequence of
integers will be represented as a string.

Tags: String
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        ret = '1'
        for k in range(1, n):
            tmp = ''
            curr = ret[0]
            count = 1
            for i in range(1, len(ret)):
                if ret[i] == curr:
                    count += 1
                else:
                    tmp += str(count) + str(curr)
                    curr = ret[i]
                    count = 1
            # Count the last one
            tmp += str(count) + str(curr)
            ret = tmp
        return ret