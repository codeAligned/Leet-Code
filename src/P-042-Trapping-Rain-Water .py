class Solution:
    # @param A, a list of integers
    # @return an integer

    # A O(n^2) worst-case solution
    def trap(self, A): 
        if not A:
            return 0
        ret = 0
        A = [(val, index) for index, val in enumerate(A)]
        curr_peak, curr_peak_index = max(A)
        # Go left
        while curr_peak_index > 1:
            value, index = max(A[:curr_peak_index])
            ret += value * (curr_peak_index - index - 1) - sum(A[i][0] for i in range(index + 1, curr_peak_index))
            curr_peak_index = index
        # Go right
        curr_peak, curr_peak_index = max(A)
        while curr_peak_index < len(A) - 1:
            value, index = max(A[curr_peak_index + 1:])
            ret += value * (index - curr_peak_index - 1) - sum(A[i][0] for i in range(curr_peak_index + 1, index))
            curr_peak_index = index
        return ret

    # O(n) Solution
    def trap(self, A):
        ret = 0
        left, right = 0, len(A) - 1 # Two pointers
        left_max = right_max = 0 # store the curr max between 0-left / right-end
        while left <= right:
            left_max = max(left_max, A[left])
            right_max = max(right_max, A[right])
            if left_max < right_max:
                ret += left_max - A[left] # this amount of water can be safely stored at position left
                left += 1
            else:
                ret += right_max - A[right]
                right -= 1
        return ret

s = Solution()
A = [0,5,6,4,6,1,0,0,2,7]
print s.trap(A)