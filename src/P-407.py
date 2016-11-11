class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = len(heightMap[0]) if m else 0

        peakMap = [[0x7FFFFFFF] * n for _ in range(m)]

        q = []

        for x in range(m):
            peakMap[x][0], peakMap[x][-1] = heightMap[x][0], heightMap[x][-1]
            q.extend([(x, 0), (x, n - 1)])
        for y in range(n):
            peakMap[0][y], peakMap[-1][y] = heightMap[0][y], heightMap[-1][y]
            q.extend([(0, y), (m - 1, y)])
        
        while q:
            x, y = q.pop(0)
            for nx, ny in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
                if nx > 0 and nx < m - 1 and ny > 0 and ny < n - 1:
                    limit = max(peakMap[x][y], heightMap[nx][ny])
                    if peakMap[nx][ny] > limit:
                        peakMap[nx][ny] = limit
                        q.append((nx, ny))
                        
        return sum(peakMap[x][y] - heightMap[x][y] for x in range(m) for y in range(n))