'''
P-120 - Triangle

Given a triangle, find the minimum path sum from top to bottom. Each
step you may move to adjacent numbers on the row below. For example,
given the following triangle[       [2],      [3,4],     [6,5,7],
[4,1,8,3]  ] The minimum path sum from top to bottom
is11(i.e.,2+3+5+1= 11). Note:Bonus point if you are able to do this
using onlyO(n) extra space, wherenis the total number of rows in the
triangle.

Tags: Array, Dynamic Programming
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        m = triangle[-1]
        for row in reversed(triangle[:-1]):
            m = [row[i] + min(m[i], m[i + 1]) for i in range(len(row))]
        return m[0]

s = Solution()
t = [[-10]]

print s.minimumTotal(t)