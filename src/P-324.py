from copy import copy

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        l = copy(nums)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = l[len(nums) / 2 + i/2]
            else:
                nums[i] = l[i/2]