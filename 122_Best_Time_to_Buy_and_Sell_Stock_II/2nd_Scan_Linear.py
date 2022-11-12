# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        Solution: Greedy
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!!
        TP:
        - if nextday_price > today_price, then we: buy today, sell tomorrow
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        prev = prices[0]
        for price in prices[1:]:
            if price > prev:
                max_profit += price - prev
            prev = price
        return max_profit
