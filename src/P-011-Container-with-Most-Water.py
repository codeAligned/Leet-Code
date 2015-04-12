'''
P-011 - Container With Most Water

Given n non-negative integers a1,a2, ...,an, where each represents a
point at coordinate (i,ai). n vertical lines are drawn such that the two
endpoints of line i is at (i,ai) and (i, 0). Find two lines, which
together with x-axis forms a container, such that the container
contains the most water. Note: You may not slant the container.

Tags: Array, Two Pointers
'''

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
