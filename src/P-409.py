class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {}
        
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        odd_list = filter(lambda x: x%2 != 0, d.values())
        
        odd_max = 0 if not odd_list else sum(odd_list) - len(odd_list) + 1
        
        even_list = filter(lambda x: x%2 == 0, d.values())
        
        even_sum = 0 if not even_list else sum(even_list)
        
        return odd_max + even_sum