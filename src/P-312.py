class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        d = [[0] * (n + 2)  for _ in range(n + 2)]
        
        nums.insert(0, 1)
        nums.append(1)
        
        for l in range(1, n + 1):
            for i in range(1, n + 2 - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    d[i][j] = max(d[i][j], nums[k] * nums[j + 1] * nums[i - 1] + d[i][k - 1] + d[k + 1][j])
                    
        return d[1][n]