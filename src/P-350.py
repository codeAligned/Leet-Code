class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        h1, h2 = dict.fromkeys(set(nums1), 0), dict.fromkeys(set(nums2), 0)
        ret = []
        
        for n in nums1:
            h1[n] += 1
        for n in nums2:
            h2[n] += 1
        
        for n in set(nums1).intersection(set(nums2)):
            ret.extend([n] * min(h1[n], h2[n]))
            
        return ret
        