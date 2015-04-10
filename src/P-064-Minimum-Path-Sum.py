class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        for x in xrange(len(grid)):
            for y in xrange(len(grid[x])):
                if x == 0 and y == 0:
                    continue
                grid[x][y] += min(                                  \
                    grid[x - 1][y] if x > 0 else grid[x][y - 1],    \
                    grid[x][y - 1] if y > 0 else grid[x - 1][y],    \
                    )
        return grid[-1][-1]
