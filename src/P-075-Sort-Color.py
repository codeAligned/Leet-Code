'''
P-075 - Sort Colors

Given an array withnobjects colored red, white or blue, sort them so
that objects of the same color are adjacent, with the colors in the
order red, white and blue. Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively. Note:You are
not suppose to use the library's sort function for this problem. click
to show follow up. Follow up:A rather straight forward solution is a
two-pass algorithm using counting sort.First, iterate the array
counting number of 0's, 1's, and 2's, then overwrite array with total
number of 0's, then 1's and followed by 2's. Could you come up with an
one-pass algorithm using only constant space?

Tags: Array, Two Pointers, Sort
'''

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