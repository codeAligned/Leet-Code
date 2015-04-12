'''
P-045 - Jump Game II

Given an array of non-negative integers, you are initially positioned
at the first index of the array. Each element in the array represents
your maximum jump length at that position. Your goal is to reach the
last index in the minimum number of jumps. For example:Given array A
=[2,3,1,1,4] The minimum number of jumps to reach the last index is2.
(Jump1step from index 0 to 1, then3steps to the last index.)

Tags: Array, Greedy
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        jumps = 0
        start = end = max_reach = 0
        while max_reach < len(A) - 1:
            for i in range(start, end + 1):
                max_reach = max(max_reach, i + A[i])
            start, end = end + 1, max_reach
            jumps += 1
        return jumps

s = Solution()
print s.jump([2,3,1,1,4])
print s.jump([3,2,1,0,4])
print s.jump([2,0,1])
print s.jump([1,1,0])