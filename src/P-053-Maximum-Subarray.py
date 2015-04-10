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