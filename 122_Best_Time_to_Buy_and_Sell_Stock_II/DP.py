# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        Solution: DP
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        Algorithm:
        - Base Case:
            - T[-1][k][0] = 0
            - T[-1][k][1] = -float('inf')
            - T[i][0][0] = 0
            - T[i][0][1] = -float('inf')
        - Recurrence:
            - T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
            - T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-1][k][0] - prices[i]) <- because k is infinity
        :type prices: List[int]
        :rtype: int
        """
        T_ik0 = 0
        T_ik1 = -float('inf')
        for price in prices:
            tmp = T_ik0 # because we were using T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i]) so we need a tmp to store old T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price)
            T_ik1 = max(T_ik1, tmp - price)
        return T_ik0

prices = [7,1,5,3,6,4]
#prices = [1,2,3,4,5]
#prices = [7,6,4,3,1]
sol = Solution()
print sol.maxProfit(prices)