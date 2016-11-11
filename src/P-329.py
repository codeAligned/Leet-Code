class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        d = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ret = 0
        
        def dfs(i, j):
            d[i][j] = 1
            
            m_ret = 0
            direc = filter(lambda (n_i, n_j): n_i >= 0 and n_i < len(matrix) and n_j >=0 and n_j < len(matrix[0]), [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
            for n_i, n_j in direc:
                if matrix[i][j] < matrix[n_i][n_j]:
                    if d[n_i][n_j] != 0:
                        m_ret = max(m_ret, d[n_i][n_j])
                    else:
                        m_ret = max(m_ret, dfs(n_i, n_j))
                
            d[i][j] += m_ret
             
            return d[i][j]
                    
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                ret = max(ret, dfs(i, j))
                
        return ret
        