class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        m = [0] * (n + 2)
        m[0] = 1
        m[1] = 2
        for k in range(2, n):
            m[k] = m[k - 1] + m[k - 2]
        return m[n - 1]

s = Solution()

print s.climbStairs(10)