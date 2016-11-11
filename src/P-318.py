class Solution(object):
    
    def bits(self, word):
        bits = 0
        for c in word:
            shift = ord(c) - ord('a')
            bits = bits | (1 << shift)
        return bits
    
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            b = self.bits(w)
            d[b] = max(d.get(b, 0), len(w))
        
        ret = 0
        
        for i in d:
            for j in d:
                if i & j == 0:
                    ret = max(ret, d[i] * d[j])
        
        return ret