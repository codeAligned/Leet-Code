class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Optimal Substructure
        # d[n] = max(max(k, d[k]) * max(n-k, d[n - k]) k = 1 to ceil(n / 2)
        
        # from math import ceil
        
        # d = [1] * (n + 1)

        # for curr_num in range(2, n + 1):
        #     for j in range(1, int(ceil(curr_num / 2)) + 1):
        #         d[curr_num] = max(d[curr_num], max(d[j], j) * max(curr_num - j, d[curr_num - j]))
                
        # return d[n]
        
        # Linear Solution
        
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 0:
            return 3 ** (n / 3)
        elif n % 3 == 1:
            return 3 ** (n / 3 - 1) * 4
        else:
            return 3 ** (n / 3) * 2