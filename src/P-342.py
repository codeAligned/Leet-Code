class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # There is one and only one '1' at the even position of the binary representation of the number
        
        if num <= 0:
            return False
            
        flag = False
        for i in reversed(range(31)):
            if not flag:
                if (num >> i) & 1 == 1:
                    if i % 2 == 0:
                        flag = True
                    else:
                        return False
            else:
                if (num >> i) & 1 == 1:
                    return False
        
        return True