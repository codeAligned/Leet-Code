from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        
        d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        
        g1 = {'z': 0, 'w': 2, 'u': 4, 'x': 6, 'g': 8}
        g2 = {'o': 1, 'h': 3, 'f': 5}
        g3 = {'s': 7, 'i': 9}
        
        c = Counter(s)
        
        for gg in (g1, g2, g3):
            found = True
            while found:
                found = False
                for g, v in gg.iteritems():
                    if g in c:
                        found = True
                        ret.append(v)
                        c -= Counter(d[v])
                
        ret.sort()
        return ''.join(str(n) for n in ret)