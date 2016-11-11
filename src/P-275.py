class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        
        for i, c in enumerate(reversed(citations)):
            if i + 1 <= c:
                h = i + 1
            else:
                break
    
        return h