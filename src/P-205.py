class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        d1 = {}
        d2 = {}
        
        for i in range(len(s)):
            if s[i] in d1:
                if d1[s[i]] != t[i] or t[i] not in d2 or d2[t[i]] != s[i]:
                    return False
            else:
                if t[i] in d2:
                    return False
                else:
                    d1[s[i]] = t[i]
                    d2[t[i]] = s[i]
                
        return True
                