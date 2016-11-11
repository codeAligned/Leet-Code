from math import sqrt

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ####### Dynamic Programming Solution - TLE - Can be improved by making d static (class member) so that multiple calls may reuse the d
        # d = [0] * (n + 1)
            
        # for i in xrange(1,  n + 1):
        #     d[i] = i
        #     for s in reversed(xrange(1, int(sqrt(i)) + 1)):
        #         d[i] = min(d[i], 1 + d[i - s * s])
                
        # return d[n]
        
        
        ####### BFS Solution
        
        q = [n]
        ret = 1
        
        while q:
            new_q = []
            for e in q:
                for k in reversed(xrange(1, int(sqrt(e)) + 1)):
                    if k * k == e:
                        return ret
                    else:
                        new_q.append(e - k * k)
            q = new_q
            ret += 1