# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, k, prices):
        """
        Solution: DP
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        Algorithm:
        - Basic idea is same as the solution
        - we need to update all the maximum profits with different k values corresponding to 0 or 1 stocks in hand at the end of the day
        - T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
        - T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
        - Optimization to avoid TLE: Determine if k > len(prices)/2 -> If the given k is no less than this value, i.e., k >= n/2, we can extend k to positive infinity
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices)/2:
            T_ik0 = 0
            T_ik1 = -float('inf')
            for price in prices:
                tmp = T_ik0
                T_ik0 = max(T_ik0, T_ik1 + price)
                T_ik1 = max(T_ik1, tmp - price)
            return T_ik0

        T_ik0 = [0 for _ in range(k+1)]
        T_ik1 = [-float('inf') for _ in range(k+1)]
        for price in prices:
            for j in reversed(range(1,k+1)):
                T_ik0[j] = max(T_ik0[j], T_ik1[j]+price)
                T_ik1[j] = max(T_ik1[j], T_ik0[j-1]-price)
        return T_ik0[k]

#prices = [2,4,1]
#k = 2
#k = 2
prices = [3,3,5,0,0,3,1,4]
k = 2
#prices = [3,2,6,5,0,3]

sol = Solution()
print sol.maxProfit(k, prices)