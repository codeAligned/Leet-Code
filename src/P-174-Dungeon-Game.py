class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer

    # hp[i][j] represents the min hp needed at position (i, j)
    # Add dummy row and column at bottom and right side
    def calculateMinimumHP(self, dungeon):
        n, m = len(dungeon), len(dungeon[0])
        d = [[2**31] * (m + 1) for _ in range(n + 1)]
        d[n][m - 1] = d[n - 1][m] = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                need = min(d[i + 1][j], d[i][j + 1]) - dungeon[i][j]
                d[i][j] = 1 if need <= 0 else need
        return d[0][0]

s = Solution()
d = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5],
]

print s.calculateMinimumHP(d)