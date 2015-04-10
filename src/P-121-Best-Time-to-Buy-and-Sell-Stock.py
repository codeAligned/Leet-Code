class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_diff = 0
        max_start = prices[0]
        for price in prices:
            max_diff = max(max_diff, price - max_start)
            max_start = min(max_start, price)
        return max_diff

s = Solution()
l = [2, 3, 4, 1, 5]

print s.maxProfit(l)