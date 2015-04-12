'''
P-198 - House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected andit will automatically contact the police
if two adjacent houses were broken into on the same night. Given a
list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob
tonightwithout alerting the police. Credits:Special thanks
to@ifanchufor adding this problem and creating all test cases. Also
thanks to@tsfor adding additional test cases.

Tags: Dynamic Programming
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        m = [0] * len(num)
        if len(num) == 0:
            return 0
        elif len(num) == 1:
            return num[0]
        elif len(num) == 2:
            return max(num[1], num[0])
        else:
            m[-1] = num[-1]
            m[-2] = max(num[-1], num[-2])
            for i in reversed(range(len(num) - 2)):
                m[i] = max(num[i] + m[i + 2], m[i + 1])
            return m[0]