# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        Algorithm:
        - T[i][k][0]: On i-th day with (at-most) k transaction and 0 stocks in hand AFTER the move
        - T[i][k][1]: On i-th day with (at-most) k transaction and 1 stocks in hand AFTER the move
        - Base Case:
            - T[-1][k][0] = 0 (no stock, no profit)
            - T[-1][k][1] = -float('inf') (IMPOSSIBLE to have 1 stock in hand ahead of time)
            - T[i][0][0] = 0 (no transaction allowed thus no profit) !!!
            - T[i][0][1] = -float('inf') (no transaction thus IMPOSSIBLE to have stock in hand) !!!
        - Recurrence Case:
            - T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices(i)) -> SELL action won't effect k
            - T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices(i)) -> BUY action will effect k
        - For this problem k == 1 thus Recurrence Case will be:
            - T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices(i))
            - T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices(i)) = max(T[i-1][1][1], -prices(i))
        - To improve the space complexity, the maximum profits on the i-th day actually only depend on those on
        the (i-1)-th day: so we can have T[i][1][0] to star with 0 (T[i][0][0]), T[i][1][1] to start with -float('inf') (T[i][0][1])
        - O(1) Solution WHY..?? T[i][k][0] 與 T[i-1][k][0] 的關係:
        T[i][k][0]即為T[i-1][k][0]在下一個循環(e.g.T[i][k][0]建立在前一循環的結果上),所以O(1) solution可以寫作:
            - T_ik0 = max(T_ik0, T_ik1 + price)
        另外T[i][k][1]與T[i-1][k][1]也可以如法泡製即:
            - T_ik1 = max(T_ik1, - price)
        :type prices: List[int]
        :rtype: int
        """
        # Base Case: T_i10 = 0, T_i11= -float('inf')
        T_i10 = 0
        T_i11 = -float('inf')
        for price in prices:
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, -price)
        return T_i10

prices = [7,1,5,3,6,4]
sol = Solution()
print sol.maxProfit(prices)
