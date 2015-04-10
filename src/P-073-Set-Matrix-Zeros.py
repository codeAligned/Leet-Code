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