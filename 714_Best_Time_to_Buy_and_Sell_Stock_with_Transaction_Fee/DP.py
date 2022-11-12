# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Algorithm:
        - T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i] - fee)
        - T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i])
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        T_ik0 = 0
        T_ik1 = -float('inf')
        for price in prices:
            tmp = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price - fee)
            T_ik1 = max(T_ik1, tmp - price)
        return T_ik0

prices = [1, 3, 2, 8, 4, 9]
fee = 2
sol = Solution()
print sol.maxProfit(prices, fee)
