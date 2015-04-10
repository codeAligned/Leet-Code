class Solution:
    # @return an integer
    def maxArea(self, h):
        i, j, m = 0, len(h) - 1, 0
        while i < j:
            m = max(m, (j - i) * min(h[i], h[j]))
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
        return m