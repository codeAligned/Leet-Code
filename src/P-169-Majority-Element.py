'''
P-169 - Majority Element

Given an array of sizen, find the majority element. The majority
element is the element that appears more than&lfloor; n/2
&rfloor;times. You may assume that the array is non-empty and the
majority element always exist in the array. Credits:Special thanks
to@tsfor adding this problem and creating all test cases.

Tags: Divide and Conquer, Array, Bit Manipulation
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        m = {}
        if len(num) == 1:
            return num[0]
        for c in num:
            if c in m:
                m[c] += 1
                if m[c] > len(num) / 2:
                    return c
            else:
                m[c] = 1

s = Solution()
print s.majorityElement([1,])