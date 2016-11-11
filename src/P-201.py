from math import ceil, log

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n == 0:
            return 0
        l = len(bin(n)) - 2
        ret = ['0'] * l
        
        for i, b in enumerate('0' * (l - len(bin(n & m)) + 2) + bin(n & m)[2:]):
            if b == '0':
                continue
            else:
                a = (1 << (l - i - 1)) - 1
                b = 1 << (l - i - 1)
                if (n | a) & ~b < m:
                    ret[i] = '1'
        
        return int(''.join(ret), 2)