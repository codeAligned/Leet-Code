'''
P-079 - Word Search

Given a 2D board and a word, find if the word exists in the grid. The
word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once. For
example,Givenboard=[    ["ABCE"],    ["SFCS"],    ["ADEE"]
]word="ABCCED", -> returnstrue,word="SEE", -> returnstrue,word="ABCB",
-> returnsfalse.

Tags: Array, Backtracking
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean

    # Recursive approach - Time limit exceeded
    def search(self, x, y, c = 0):
        ret = False
        if self.board[x][y] == self.word[c]:
            if c + 1 == len(self.word):
                return True
            # mark the visited cell
            self.board[x][y] = '*'
            # up
            if x > 0:
                ret |= self.search(x - 1, y, c + 1)
            # down
            if x < self.m - 1:
                ret |= self.search(x + 1, y, c + 1)
            # right
            if y < self.n - 1:
                ret |= self.search(x, y + 1, c + 1)
            # left
            if y > 0:
                ret |= self.search(x, y - 1, c + 1)
            # unmark the cell
            self.board[x][y] = self.word[c]
        return ret

    def exist(self, board, word):
        self.board = board
        self.word = word
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.search(i, j):
                    return True
        return False

    # Iterative approach
    def exist(self, board, word):
        stack = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                stack.append((i, j, 0, False))
                while stack:
                    x, y, c, v = stack.pop()
                    if v:
                        board[x][y] = word[c]
                    elif board[x][y] == word[c]:
                        board[x][y] = '*'
                        if c + 1 == len(word):
                            return True
                        stack.append((x, y, c, True))
                        # up
                        if x > 0:
                            stack.append((x - 1, y, c + 1, False))
                        # down
                        if x < m - 1:
                            stack.append((x + 1, y, c + 1, False))
                        # left
                        if y < n - 1:
                            stack.append((x, y + 1, c + 1, False))
                        # right
                        if y > 0:
                            stack.append((x, y - 1, c + 1, False))
        return False

s = Solution()
b = [
  list("ABCE"),
  list("SFCS"),
  list("ADEE")
]
w = 'ABCESEEDASA'
'''
b = [
    list("aaaa"),
    list("aaaa"),
    list("aaaa"),
]
w = "aaaaaaaaaaaaa"
'''
print s.exist(b, w)