class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, r):
        n = len(r)
        if n <= 1:
            return n
        c = [1] * n
        # First Pass check my left neighbor
        for i in range(1, n):
            if r[i] > r[i - 1]:
                c[i] = c[i - 1] + 1
        # Second Pass check my right neighbor
        for i in range(n - 1, 0, -1):
            if r[i - 1] > r[i]:
                c[i - 1] = max(c[i] + 1, c[i - 1])
        return sum(c)