class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        h = len(s) - 1
        
        s = list(s)
        
        v = set(['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U'])
        
        while l < h and l < len(s) and h >= 0:
            while s[l] not in v and l < len(s) - 1:
                l += 1
            while s[h] not in v and h > 0:
                h -= 1
            if l < h and s[l] in v and s[h] in v:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
                
        return ''.join(s)