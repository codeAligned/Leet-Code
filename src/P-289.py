class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        
        for x in range(m):
            for y in range(n):
                total_live = 1 # use positive/negative to indicate whether the original cell is live/dead. Plus 1 to skip 0
                for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1)]:
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] > 0:
                        total_live += 1
                if board[x][y] == 1 :
                    board[x][y] = total_live
                else:
                    board[x][y] = -(total_live - 1)
        
        for x in range(m):
            for y in range(n):
                total_live = board[x][y] - 1 if board[x][y] > 0 else -board[x][y]
                is_live = board[x][y] > 0
                
                if is_live:
                    if total_live < 2 or total_live > 3:
                        board[x][y] = 0
                        continue
                    else:
                        board[x][y] = 1
                        continue
                elif total_live == 3:
                    board[x][y] = 1
                else:
                    board[x][y] = 0
                