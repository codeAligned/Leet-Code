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