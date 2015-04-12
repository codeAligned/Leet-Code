'''
P-059 - Spiral Matrix II

Given an integern, generate a square matrix filled with elements from
1 ton2in spiral order. For example,Givenn=3,

Tags: Array
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = [[0] * n for i in range(n)]
        x, y, m, n, k = 0, 0, len(matrix) - 1, len(matrix[0]) - 1, 1
        while x <= m and y <= n:
            for j in xrange(y, n + 1):
                matrix[x][j] = k
                k += 1
            x += 1
            for i in xrange(x, m + 1):
                matrix[i][n] = k
                k += 1
            n -= 1
            if x <= m:
                for j in reversed(xrange(y, n + 1)):
                    matrix[m][j] = k
                    k += 1
            m -= 1
            if y <= n:
                for i in reversed(xrange(x, m + 1)):
                    matrix[i][y] = k
                    k += 1
            y += 1
        return matrix

s = Solution()
m = s.generateMatrix(3)

for row in m:
    for item in row:
        print "%3d" % item,
    print