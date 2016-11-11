class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        bv = 0
        
        for c in s + t:
            bv ^= (1 << (ord(c) - ord('a')))
            
        for i in range(26):
            if (bv >> i) & 1:
                return chr(ord('a') + i)
        