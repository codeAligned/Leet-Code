'''
P-122 - Best Time to Buy and Sell Stock II

Say you have an array for which theithelement is the price of a given
stock on dayi. Design an algorithm to find the maximum profit. You may
complete as many transactions as you like (ie, buy one and sell one
share of the stock multiple times). However, you may not engage in
multiple transactions at the same time (ie, you must sell the stock
before you buy again).

Tags: Array, Greedy
'''

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