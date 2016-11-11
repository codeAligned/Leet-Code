class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num_keep = len(num) - k
        
        s = []
        
        for i, c in enumerate(num):
            if i != 0:
                while s and int(c) < int(s[-1]) and len(s) + len(num) - i > num_keep:
                    s.pop()
            if len(s) < num_keep:
                s.append(c)
        
        return str(int(''.join(s) if s else '0'))