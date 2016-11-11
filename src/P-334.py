class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        small = 1 << 32
        large = 1 << 32
        
        for n in nums:
            if n <= small:
                small = n
            elif n <= large:
                large = n
            else:
                return True
                
        return False