class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        cnt = dict.fromkeys(s, 0)
        for c in s:
            cnt[c] += 1
            
        for c in filter(lambda x: cnt[x] < k, cnt.keys()):
            return max(self.longestSubstring(sub_str, k) for sub_str in s.split(c))
        
        return len(s)