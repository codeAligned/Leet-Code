class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        m = triangle[-1]
        for row in reversed(triangle[:-1]):
            m = [row[i] + min(m[i], m[i + 1]) for i in range(len(row))]
        return m[0]

s = Solution()
t = [[-10]]

print s.minimumTotal(t)