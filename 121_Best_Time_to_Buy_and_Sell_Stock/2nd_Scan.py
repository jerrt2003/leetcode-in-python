# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - keep tracking of max_profit and min_prices
        :type prices: List[int]
        :rtype: int
        """
        max_profit = -float('inf')
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

prices = [7,6,4,3,1,9]
print Solution().maxProfit(prices)