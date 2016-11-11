class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        A_sum = sum(A)
        ret = sum(idx * val for idx, val in enumerate(A))
        last = ret
        
        for v in reversed(A):
            tmp = last + A_sum - n * v
            ret = max(tmp, ret)
            last = tmp
            
        return ret