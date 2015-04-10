class Solution:
    # @param A a list of integers
    # @return nothing, sort in place

    # One-pass Solution
    def sortColors(self, A):
        # red -> 0, white -> 1, blue -> 2
        r = w = b = -1
        for c in A:
            if c == 0:
                b += 1; w += 1; r += 1
                A[b] = 2; A[w] = 1; A[r] = 0
            if c == 1:
                b += 1; w += 1
                A[b] = 2; A[w] = 1
            if c == 2:
                b += 1
                A[b] = 2

    # We can do two-pass
    # Count each color in the first pass
    # and fill them into the array in the second pass