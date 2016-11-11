class Solution(object):
    
    def get_digits_sum(self, n):
        t = 10
        ret = (n % t) * (n % t)
        
        while n >= t:
            d = (n / t) % 10
            ret += d * d
            t *= 10
            
        return ret
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set([n])
        nn = n
        while True:
            s = self.get_digits_sum(nn)
            if s == 1:
                return True
            elif s in d:
                return False
            else:
                d.add(s)
            nn = s
            