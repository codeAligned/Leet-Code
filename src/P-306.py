class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        ln = int(num)
        
        def n(i, j):
            ret = (ln % (10 ** (len(num) - i))) / (10 ** (len(num) - j))
            if len(str(ret)) != j - i:
                return -9999
            return ret
            
        def verify(n1, n2, k):
            # if num[k] == '0':
            #     return False
            n3 = n1 + n2
            i = k + 1
            while i <= len(num):
                if n(k, i) == n3:
                    if i == len(num):
                        return True
                    else:
                        return verify(n2, n3, i)
                elif n(k, i) < n3:
                    i += 1
                else:
                    break
            return False
            
        for i in range(1, len(num) / 2 + 1):
            for j in range(1, len(num) / 2 + 1):
                if len(num) - i - j < max(i, j):
                    break
                if verify(n(0, i), n(i, i + j), i + j):
                    return True
                else:
                    continue

        return False