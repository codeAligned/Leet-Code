class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        l = 0
        h = num
        
        while l <= h:
            m = (l + h) / 2
            if m * m > num:
                h = m - 1
            elif m * m < num:
                l = m + 1
            else:
                return True
                
        return False