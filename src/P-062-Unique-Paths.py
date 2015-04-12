'''
P-062 - Unique Paths

A robot is located at the top-left corner of amxngrid (marked 'Start'
in the diagram below). The robot can only move either down or right at
any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below). How many
possible unique paths are there? Above is a 3 x 7 grid. How many
possible unique paths are there? Note:mandnwill be at most 100.

Tags: Array, Dynamic Programming
'''

class Solution:
    # @return an integer

    # Combination-Math-based solution
    def uniquePaths(self, m, n):
        from math import factorial as f
        return f(m + n - 2) / f(m - 1) / f(n - 1)

    # DP-based solution
    def uniquePaths(self, m, n):
        d = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    d[i][j] = 1
                elif i == 0:
                    d[i][j] = d[i][j - 1]
                elif j == 0:
                    d[i][j] = d[i - 1][j]
                else:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]
        return d[-1][-1]

s = Solution()
print s.uniquePaths(5, 6)