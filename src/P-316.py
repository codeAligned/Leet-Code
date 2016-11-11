from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ret = ''
        count = Counter(s)       
        used = dict.fromkeys(count, False)
        
        for c in s:
            count[c] -= 1
            if not used[c]:
                while ret and ret[-1] > c and count[ret[-1]] > 0: # When then string is not empty, remove the last character (L) when c is smaller than L and L hasn't been all used, i.e., L will be encounter in the future (resulting a smaller string in lexicographical order) 
                    used[ret[-1]] = False
                    ret = ret[:-1]  # Remove the last character
                ret += c    # Append c to the string ret
                used[c] = True
                
        return ret