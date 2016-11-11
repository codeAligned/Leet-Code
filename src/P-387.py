from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = Counter(s)
        
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
                
        return -1
        