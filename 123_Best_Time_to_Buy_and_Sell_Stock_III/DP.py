# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems/111002
        Algorithm:
        - T[i][k][0]: maximum profit at the end of the i-th day with (at most) k transactions and with 0 stock in our hand AFTER taking the action
        - T[i][k][1]: maximum profit at the end of the i-th day with (at most) k transactions and with 1 stock in our hand AFTER taking the action
        ?? - k 代表"已發生"的交易次數,而不是還剩下的交易次數 ?? <--
        k: max allowed transaction
        - Base Case:
            - T[-1][k][0] = 0 (no stock in hand thus no profit)
            - T[-1][k][1] = -int('inf') (it is impossible to have stock at beginning (i is -1)
            - T[i][0][0] = 0 (k=0 -> no transaction allowed-> no profit)
            - T[i][0][1] = -int('inf') (it is impossible to buy('have') stock in hand but no transaction allowed)
        - Recurrence relations:
            - T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + price[i]) -> sell doesn't effect k
            - T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - price[i]) -> buy effect k thus k-1
            - return T[i][k][0]
        - With k = 2 (this case):
            - T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + price[i])
            - T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - price[i])
            - T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + price[i])
            - T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - price[i]) = max(T[i-1][1][1], -price[i])
        :type prices: List[int]
        :rtype: int
        """
        T_i20 = 0 # T[i][k][0] = 0
        T_i21 = -float('inf') # T[i]
        T_i10 = 0 # T[i][k][0] = 0
        T_i11 = -float('inf')
        for idx in range(len(prices)):
            '''
            T_i20 = max(T_i20, T_i21 + prices[idx])
            T_i21 = max(T_i21, T_i10 - prices[idx])
            T_i10 = max(T_i10, T_i11 + prices[idx])
            T_i11 = max(T_i11, -prices[idx])
            '''
            T_i11 = max(T_i11, -prices[idx])
            T_i10 = max(T_i10, T_i11 + prices[idx])
            T_i21 = max(T_i21, T_i10 - prices[idx])
            T_i20 = max(T_i20, T_i21 + prices[idx])
        return T_i20

prices = [3,3,5,0,0,3,1,4]
#prices = [1,2,3,4,5]
#prices = [7,6,4,3,1]
sol = Solution()
print sol.maxProfit(prices)

