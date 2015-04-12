'''
P-130 - Surrounded Regions

Given a 2D board containing'X'and'O', capture all regions surrounded
by'X'. A region is captured by flipping all'O's into'X's in that
surrounded region. For example,X X X X  X O O X  X X O X  X O X X
After running your function, the board should be:X X X X  X X X X  X X
X X  X O X X

Tags: Breadth-first Search
'''

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def bfs_push(self, stack, m, n):
        if n >= 0 and m >= 0 and n < self.j_max and m < self.i_max:
            if self.board[m][n] == 'O' and self.aux[m][n] == 0:
                stack.append((m, n))

    def bfs(self, i, j):
        stack = [(i, j)]
        region = []
        flag = True
        while stack:
            m, n = stack.pop()
            self.aux[m][n] = 1
            region.append((m, n))
            self.bfs_push(stack, m, n - 1) # Left
            self.bfs_push(stack, m, n + 1) # Right
            self.bfs_push(stack, m - 1, n) # Up
            self.bfs_push(stack, m + 1, n) # Down
        for i, j in region:
            if i == self.i_max - 1 or i == 0 or j == 0 or j == self.j_max - 1:
                flag = False
                break
        if flag:
            for i, j in region:
                self.board[i][j] = 'X'

    def solve(self, board):
        self.board = board
        self.i_max = len(board)
        if self.i_max == 0:
            return
        self.j_max = len(board[0])
        if self.j_max == 0:
            return
        self.aux = [[0] * len(row) for row in board]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.board[i][j] == 'O' and self.aux[i][j] == 0:
                    self.bfs(i, j)

b = [
    ['X', 'X', 'X', 'X', ],
    ['X', 'O', 'O', 'X', ],
    ['X', 'X', 'O', 'X', ],
    ['X', 'O', 'X', 'X', ],
]

s = Solution()
s.solve(b)
for row in b:
    print row