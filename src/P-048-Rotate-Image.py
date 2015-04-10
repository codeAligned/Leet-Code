class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix) - 1
        for x in range((n + 1) / 2):
            for y in range(x, n - x):
                matrix[x][y], matrix[y][n - x], matrix[n - x][n - y], matrix[n - y][x] = \
                matrix[n - y][x], matrix[x][y], matrix[y][n - x], matrix[n - x][n - y]
        return matrix

s = Solution()
image = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
s.rotate(image)
print image