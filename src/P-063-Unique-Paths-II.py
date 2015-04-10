from math import factorial as f

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer

    # DP-based Solution
    def uniquePathsWithObstacles(self, g):
        if g[0][0] == 1:
            return 0
        else: 
            g[0][0] = 1
        for x in xrange(len(g)):
            for y in xrange(len(g[x])):
                if x == 0 and y == 0:
                    continue
                elif g[x][y] == 1:
                    g[x][y] = 0
                else:
                    if x > 0:
                        g[x][y] += g[x - 1][y]
                    if y > 0:
                        g[x][y] += g[x][y - 1]
        return g[-1][-1]

s = Solution()
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print s.uniquePathsWithObstacles(grid)