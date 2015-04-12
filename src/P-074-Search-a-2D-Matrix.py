'''
P-074 - Search a 2D Matrix

Write an efficient algorithm that searches for a value in anmxnmatrix.
This matrix has the following properties: Integers in each row are
sorted from left to right.The first integer of each row is greater
than the last integer of the previous row. For example, Consider the
following matrix: Giventarget=3, returntrue.

Tags: Array, Binary Search
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def bin_search(self, A, i, j):
        if i > j:
            return j
        m = (i + j) / 2
        if A[m] > self.target:
            return self.bin_search(A, i, m - 1)
        elif A[m] < self.target:
            return self.bin_search(A, m + 1, j)
        else:
            return m

    def searchMatrix(self, matrix, target):
        self.target = target
        m, n = len(matrix), len(matrix[0])
        r = self.bin_search([row[0] for row in matrix], 0, m - 1)
        if r < 0:
            return False
        c = self.bin_search(matrix[r], 0, n - 1)
        if c < 0:
            return False
        return matrix[r][c] == target

s = Solution()
m = [
    [-9,-7,-7,-7,-6,-6,-6,-4,-3,-1,0],
    [3,5,6,8,8,10,12,14,14,16,17],
    [20,22,23,23,23,23,25,25,27,28,28],
    [29,31,33,33,35,37,37,39,39,41,42],
    [43,45,46,48,49,50,50,51,51,53,53],
    [56,57,58,58,58,58,58,60,61,62,64],
    [65,67,68,70,72,74,74,76,76,76,77],
    [78,79,79,80,81,82,83,85,87,89,90],
    [92,94,96,98,99,100,100,102,102,103,105],
    [106,106,106,108,109,111,113,115,117,119,120],
    [123,124,126,128,128,130,131,131,132,132,133],
    [134,136,138,140,140,142,144,145,146,148,150],
    [152,153,154,156,158,159,161,163,165,166,167],
    [170,171,173,173,173,173,174,175,176,178,180],
    [181,182,184,186,187,189,191,193,195,196,196],
]

print s.searchMatrix(m, 10)