'''
P-174 - Dungeon Game

table.dungeon, .dungeon th, .dungeon td {    border:3px solid black;
}     .dungeon th, .dungeon td {      text-align: center;      height:
70px;      width: 70px;  } The demons had captured the princess (P)
and imprisoned her in the bottom-right corner of a dungeon. The
dungeon consists of M x N rooms laid out in a 2D grid. Our valiant
knight (K) was initially positioned in the top-left room and must
fight his way through the dungeon to rescue the princess. The knight
has an initial health point represented by a positive integer. If at
any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health
(negativeintegers) upon entering these rooms;   other rooms are either
empty (0's) or contain magic orbs that increase the knight's health
(positiveintegers). In order to reach the princess as quickly as
possible, the knight decides to move only rightward or downward in
each step. Write a function to determine the knight's minimum initial
health so that he is able to rescue the princess. For example, given
the dungeon below, the initial health of the knight must be at
least7if he follows the optimal pathRIGHT-> RIGHT -> DOWN -> DOWN.
Notes:The knight's health has no upper bound.Any room can contain
threats or power-ups, even the first room the knight enters and the
bottom-right room where the princess is imprisoned. Credits:Special
thanks to@stellarifor adding this problem and creating all test cases.

Tags: Dynamic Programming, Binary Search
'''

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