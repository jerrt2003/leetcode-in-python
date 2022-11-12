# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Algorithm:
        General Recursion said that..
        - Base case: T[i][0][0] = 0, T[i][0][1] = -float('inf')
        - T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        - T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
        However we consider 2 point:
        a. k = +Infinity thus k = k-1 so T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i])
        b. cool-down is 1 day thus: T[i][k][1] = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
        :type prices: List[int]
        :rtype: int
        """
        T_ik0 = 0
        T_ik1 = -float('inf')
        T_ik0_pre = 0 # stands for T[i-2][k][0]
        for price in prices:
            tmp = T_ik0
            T_ik0 = max(T_ik0, T_ik1 + price)
            T_ik1 = max(T_ik1, T_ik0_pre - price)
            T_ik0_pre = tmp #即尚未變動前的T_ik0
        return T_ik0

prices = [1,2,3,0,2]
sol = Solution()
print sol.maxProfit(prices)