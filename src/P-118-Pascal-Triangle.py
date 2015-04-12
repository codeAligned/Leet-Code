'''
P-118 - Pascal&#39;s Triangle

GivennumRows, generate the firstnumRowsof Pascal's triangle. For
example, givennumRows= 5,Return[       [1],      [1,1],     [1,2,1],
[1,3,3,1],   [1,4,6,4,1]  ]

Tags: Array
'''

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        ret = [[1]]
        for k in range(1, numRows):
            tmp = [1] * (k + 1)
            for i in range(1, k):
                tmp[i] = ret[-1][i] + ret[-1][i - 1]
            ret.append(tmp)
        return ret

s = Solution()

for k in s.generate(1):
    print k