import os
import copy

# DFS-based Solution
# Faster but not more space complexity, not necessarily in-place
class Solution2:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        res = self.dfs(board)
        for n, row in enumerate(res):
            board[n] = ''.join(row)

    def dfs(self, board):
        stack = [board]
        while stack:
            s = stack.pop()
            result = self.fill_board(s)
            if result == 'complete':
                return s
            for r in result:
                stack.append(r)

    def fill_board(self, board):
        digits = set('123456789')
        choice, best = {}, []
        for j in range(9):
            for i in range(9):
                if board[j][i] == '.':
                    square = {board[j//3*3+y][i//3*3+x]
                              for y in range(3) for x in range(3)}
                    row = {board[j][x] for x in range(9)}
                    col = {board[y][i] for y in range(9)}
                    rest = digits.difference(square, row, col)
                    if len(rest) == 1:
                        board[j][i] = rest.pop()
                        return self.fill_board(board)
                    elif len(rest) == 0:
                        return ''
                    else:
                        choice[(j, i)] = rest
        if not choice:
            return 'complete'
        y, x = min(choice, key=lambda k: len(choice[k]))
        for n in choice[(y, x)]:
            b = copy.deepcopy(board)
            b[y][x] = n
            best.append(b)
        return best

# Another Solution
# Slower but more likely to be in-place
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def get_avail(self, board, x, y):
        if board[y][x] != '.':
            return '.'
        row = set(board[y])
        col = set(board[i][x] for i in range(9))
        grid = set(board[y / 3 * 3 + i][x / 3 * 3 + j] for i in range(3) for j in range(3))
        return set('123456789').difference(row, col, grid)

    def set_board(self, board, x, y, num):
        ret = []
        if board[y][x] == '.':
            board[y][x] = num
            for i in range(x + 1, 9):
                if self.avail_num[y][i] != '.' and num in self.avail_num[y][i]:
                    self.avail_num[y][i].discard(num)
                    ret.append((y, i))
            for j in range(y + 1, 9):
                if self.avail_num[j][x] != '.' and num in self.avail_num[j][x]:
                    self.avail_num[j][x].discard(num)
                    ret.append((j, x))
            for j in range(x + 1, (x / 3 + 1) * 3):
                if self.avail_num[y][j] != '.' and num in self.avail_num[y][j]:
                    self.avail_num[y][j].discard(num)
                    ret.append((y, j))
            for i in range(y + 1, (y / 3 + 1) * 3):
                for j in range(x / 3 * 3, (x / 3 + 1) * 3):
                    if self.avail_num[i][j] != '.' and num in self.avail_num[i][j]:
                        self.avail_num[i][j].discard(num)
                        ret.append((i, j))
        return ret

    def clr_board(self, board, x, y, l):
        if board[y][x] != '.':
            for i, j in l:
                self.avail_num[i][j].add(board[y][x])
            board[y][x] = '.'

    def solve(self, board, k = 0):
        if k == 81:
            return True
        x, y = k % 9, k / 9
        if self.avail_num[y][x] == '.':
            return self.solve(board, k + 1)
        elif len(self.avail_num[y][x]) == 0:
            return False
        else:
            for num in self.avail_num[y][x]:
                l = self.set_board(board, x, y, num)
                if self.solve(board, k + 1):
                    return True
                else:
                    self.clr_board(board, x, y, l)
            return False
 
    def solveSudoku(self, board):
        self.avail_num = [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                self.avail_num[i][j] = self.get_avail(board, j, i)
        self.solve(board)

    def print_board(self, board):
        os.system('cls')
        for row in board:
            for num in row:
                print num,
            print

s = Solution()
l = [list("........."),
     list("......3.."),
     list("...18...."),
     list("...7....."),
     list("....1.97."),
     list("........."),
     list("...36.1.."),
     list("........."),
     list(".......2.")
     ]

l = [list("..9748..."),
     list("7........"),
     list(".2.1.9..."),
     list("..7...24."),
     list(".64.1.59."),
     list(".98...3.."),
     list("...8.3.2."),
     list("........6"),
     list("...2759.."),
     ]


s.solveSudoku(l)

for r in l:
    print r