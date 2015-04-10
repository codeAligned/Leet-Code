class Solution:
    # @param height, a list of integer
    # @return an integer

    # Use a stack to keep track of the histogram 
    # on my left that are greater than me
    # We only compare i with those because the they are 
    # the only possiblities of higher area
    def largestRectangleArea(self, height):
        # Use 0 in the end as the guard
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                size = max(size, h * w)
            stack.append(i)
        return size