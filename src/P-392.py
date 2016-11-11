class Solution(object):
    def isSubsequence(self, t, s):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not t:
            return True
        
        if len(t) > len(s):
            return False
        
        i, j = 0, 0
        
        while i < len(s):
            if t[j] == s[i]:
                j += 1
            if j == len(t):
                return True
            i += 1
        
        return False