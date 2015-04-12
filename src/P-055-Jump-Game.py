'''
P-055 - Jump Game

Given an array of non-negative integers, you are initially positioned
at the first index of the array. Each element in the array represents
your maximum jump length at that position. Determine if you are able
to reach the last index. For example:A =[2,3,1,1,4], returntrue. A
=[3,2,1,0,4], returnfalse.

Tags: Array, Greedy
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean

    # Solution 1 From end to the start
    def canJump(self, A):
        goal, curr = len(A) - 1, len(A) - 2
        while curr > 0:
            if A[curr] + curr >= goal:
                goal = curr
            curr -= 1
        return A[0] >= goal

    # Solution 2 from the start to the end
    def canJump(self, A):
        jump_left = 0
        for curr, value in enumerate(A):
            # go 1 step to this cell or go all the way to the furthest
            jump_left = max(jump_left - 1, value)
            if jump_left == 0:
                break
        return curr == len(A) - 1

s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])
print s.canJump([2,0,1])
print s.canJump([1,1,0])