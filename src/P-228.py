class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        out = []
        
        st = None
        sp = None
        
        for n in nums:
            if st is None:
                st = n
            elif sp is None:
                if n == st + 1:
                    sp = n
                else:
                    out.append(str(st))
                    st = n
            else:
                if n == sp + 1:
                    sp = n
                else:
                    out.append(str(st) + '->' + str(sp))
                    st = n
                    sp = None
        
        if st is not None and sp is not None:
            out.append(str(st) + '->' + str(sp))
        elif st is not None and sp is None:
            out.append(str(st))
        
        return out