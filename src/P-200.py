class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def explore(i, j, k):
            if j > 0:
                if grid[i][j - 1] == '1':
                    grid[i][j - 1] = k
                    explore(i, j - 1, k)
            if j < len(grid[0]) - 1:
                if grid[i][j + 1] == '1':
                    grid[i][j + 1] = k
                    explore(i, j + 1, k)
            if i > 0:
                if grid[i - 1][j] == '1':
                    grid[i - 1][j] = k
                    explore(i - 1, j, k)
            if i < len(grid) - 1:
                if grid[i + 1][j] == '1':
                    grid[i + 1][j] = k
                    explore(i + 1, j, k)
            
        k = 2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = k
                    explore(i, j, k)
                    k += 1
                    #print i, j, k
        
        return k - 2            