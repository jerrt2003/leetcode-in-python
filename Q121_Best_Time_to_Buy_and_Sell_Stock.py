class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = sell_price = 0
        for price in prices[::-1]:
            sell_price = max(price, sell_price)
            profit = sell_price - price
            max_profit = max(profit, max_profit)
        return max_profit


a = [7,1,5,3,6,4]
b = [7,6,4,3,1]
sol = Solution()
print sol.maxProfit(b)