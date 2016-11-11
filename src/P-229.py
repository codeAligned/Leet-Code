class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        m1, m2, c1, c2 = None, None, 0, 0
        
        for n in nums:
            if n == m1:
                c1 += 1
            elif n == m2:
                c2 += 1
            elif c1 == 0:
                c1 += 1
                m1 = n
            elif c2 == 0:
                c2 += 1
                m2 = n
            else:
                c1 -= 1
                c2 -= 1

        ret = []
        if m1 != None and nums.count(m1) > len(nums) / 3:
            ret.append(m1)
        if m2 != None and nums.count(m2) > len(nums) / 3:
            ret.append(m2)
            
        return ret