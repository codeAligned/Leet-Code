class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_dict = {}
        m_dict = {}
        
        for c in ransomNote:
            if c in r_dict:
                r_dict[c] += 1
            else:
                r_dict[c] = 0
                
        for c in magazine:
            if c in m_dict:
                m_dict[c] += 1
            else:
                m_dict[c] = 0
        
        for k in r_dict.keys():
            if k in m_dict and r_dict[k] <= m_dict[k]:
                continue
            else:
                return False
        return True