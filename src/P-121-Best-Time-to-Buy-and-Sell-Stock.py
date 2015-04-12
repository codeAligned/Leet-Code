'''
P-121 - Best Time to Buy and Sell Stock

Say you have an array for which theithelement is the price of a given
stock on dayi. If you were only permitted to complete at most one
transaction (ie, buy one and sell one share of the stock), design an
algorithm to find the maximum profit.

Tags: Array, Dynamic Programming
'''

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