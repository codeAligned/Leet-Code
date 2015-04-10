class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def max_subarray_circular(self, A):
        max_ending_here = max_so_far = A[0]
        max_start = max_end = start = 0
        for curr in range(1, len(A) * 2):
            curr = curr % len(A)
            if A[curr] > max_ending_here + A[curr]:
                start = curr
            max_ending_here = max(A[curr], max_ending_here + A[curr])
            if max_so_far < max_ending_here:
                max_start = start
                max_end = curr
            max_so_far = max(max_so_far, max_ending_here)
        #return max_so_far, max_start, max_end + 1
        return max_start
        
    def canCompleteCircuit(self, gas, cost):
        left = [g - c for g, c in zip(gas, cost)]
        return -1 if sum(left) < 0 else self.max_subarray_circular(left)

s = Solution()
#print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
#print s.canCompleteCircuit([1, 2], [2, 1])
#print s.canCompleteCircuit([1,2,3,3], [2,1,5,1])
print s.canCompleteCircuit([5,5,5,5], [3,4,9,3])