class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
        ret = 0
        curr = 0
        
        for num in nums:
            if curr >= n:
                return ret
            if num <= curr + 1:
                curr += num
            else:
                while curr + 1 < num:
                    ret += 1
                    curr += (curr + 1)
                    if curr >= n:
                        return ret
                curr += num
                
        while curr < n:
            ret += 1
            curr += (curr + 1)
            
        return ret