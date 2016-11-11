class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        # Convert decimal number n to base-d digits in list
        def divide(l, n, d):
            l.insert(0, n % d)
            if n / d != 0:
                divide(l, n / d, d)
        
        l = []
            
        divide(l, num if num >=0 else (1 << 32) + num, 16)
        
        # Map each digit to its coorespoding letter
        return ''.join(map(lambda x: str(x) if x < 10 else chr(ord('a') + x - 10), l))