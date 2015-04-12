'''
P-073 - Set Matrix Zeroes

Given amxnmatrix, if an element is 0, set its entire row and column to
0. Do it in place. click to show follow up. Did you use extra space?A
straight forward solution using O(mn) space is probably a bad idea.A
simple improvement uses O(m+n) space, but still not the best
solution.Could you devise a constant space solution?

Tags: Array
'''

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        try:
            m = len(matrix)
            n = len(matrix[0])
        except IndexError:
            return
        row, col = set(), set()
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    row.add(x)
                    col.add(y)
        for x in range(m):
            for y in range(n):
                if x in row or y in col:
                    matrix[x][y] = 0