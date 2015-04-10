class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return sum([y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y])

s = Solution()
l = [2, 3, 4, 1, 5]
l = [8, 4, 2, 1]
l = [1, 4, 2]
l = [1, 2, 4]

print s.maxProfit(l)