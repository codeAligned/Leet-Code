class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sd, gd = {}, {}
        bull, cow = 0, 0
        
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                for c, d in ((s, sd), (g, gd)):
                    d[c] = d[c] + 1 if c in d else 1
                        
        cow = reduce(lambda s, k: s + min(sd[k], gd[k]), sd.viewkeys() & gd.viewkeys(), 0)
        
        return str(bull)+'A'+str(cow)+'B'