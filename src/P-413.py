class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
            
        diff = [A[i + 1] - A[i] for i in range(len(A) - 1)]
        
        curr_diff = diff[0]
        prev_pos = 0
        
        ret = 0
        
        for i, d in enumerate(diff):
            if d == curr_diff:
                continue
            else:
                curr_diff = d
                if i - prev_pos >= 2:
                    length = i - 1 - prev_pos + 2
                    ret += (length - 1)*(length - 2)/2
                prev_pos = i
        
        if i - prev_pos >= 1:
            length = i - prev_pos + 2
            ret += (length - 1)*(length - 2)/2
        
        return ret