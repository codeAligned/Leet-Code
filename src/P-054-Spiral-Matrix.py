'''
P-054 - Spiral Matrix

Given a matrix ofmxnelements (mrows,ncolumns), return all elements of
the matrix in spiral order. For example,Given the following matrix:
You should return[1,2,3,6,9,8,7,4,5].

Tags: Array
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers

    # Solution that not touch the matrix
    def spiralOrder(self, matrix):
        ret = []
        if not matrix:
            return ret
        # current row-head, row-end, column-head, column-end
        x, y, m, n = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while x <= m and y <= n:
            for j in xrange(y, n + 1):
                ret.append(matrix[x][j])
            x += 1
            for i in xrange(x, m + 1):
                ret.append(matrix[i][n])
            n -= 1
            if x <= m:
                for j in reversed(xrange(y, n + 1)):
                    ret.append(matrix[m][j])
            m -= 1
            if y <= n:
                for i in reversed(xrange(x, m + 1)):
                    ret.append(matrix[i][y])
            y += 1
        return ret

    # Solution that touches the matrix
    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
        
s = Solution()
m = [
    [ 1, 2, 3, 4, 4, 4],
    [ 5, 6, 7, 8, 8, 8],
    [ 9,10,11,12,12,12],
    [13,14,15,16,16,16],
    [17,18,19,20,21,22],
    [23,24,25,26,27,28],
    [29,30,31,32,33,34]
]
m = [[1, 2, 3]]
#m = [[1], [2], [3]]
print s.spiralOrder(m)