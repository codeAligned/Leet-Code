'''
P-053 - Maximum Subarray

Find the contiguous subarray within an array (containing at least one
number) which has the largest sum. For example, given the
array[&#8722;2,1,&#8722;3,4,&#8722;1,2,1,&#8722;5,4],the contiguous
subarray[4,&#8722;1,2,1]has the largest sum =6. click to show more
practice. If you have figured out the O(n) solution, try coding
another solution using the divide and conquer approach, which is more
subtle.

Tags: Divide and Conquer, Array, Dynamic Programming
'''

class Solution:
    # @param A, a list of integers
    # @return an integer

    # DP-based Solution
    def maxSubArray(self, A):
        curr_max = max_sum = A[0]
        max_start = max_end = 0
        curr_start = 0
        for i in range(1, len(A)):
            if curr_max + A[i] < A[i]:
                curr_start = i
            curr_max = max(A[i], curr_max + A[i])
            if max_sum < curr_max:
                max_end = i
                max_start = curr_start
            max_sum = max(max_sum, curr_max)
        return max_sum

    '''
    def maxSubArray(self, A):
        curr_max = max_sum = A[0]
        for v in A[1:]:
            curr_max = max(v, curr_max + v)
            max_sum = max(max_sum, curr_max)
        return max_sum
    '''