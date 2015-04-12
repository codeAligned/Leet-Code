'''
P-189 - Rotate Array

Rotate an array ofnelements to the right byksteps. For example, withn=
7 andk= 3, the array[1,2,3,4,5,6,7]is rotated to[5,6,7,1,2,3,4].
Note:Try to come up as many solutions as you can, there are at least 3
different ways to solve this problem. [show hint] Related
problem:Reverse Words in a String II Credits:Special thanks
to@Freezenfor adding this problem and creating all test cases.

Tags: Array
'''

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k, s = 0):
        i = 0
        l = len(nums) - s
        if l > 0:
            k %= l
            for i in range(k):
                nums[s + i], nums[s + i + l - k] =\
                nums[s + i + l - k], nums[s + i]
            self.rotate(nums, k, s + i + 1)

s = Solution()
l = [1,2,3,4,5,6,7]
s.rotate(l,11)
print l