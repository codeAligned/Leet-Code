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