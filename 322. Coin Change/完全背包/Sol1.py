# -*- coding: utf-8 -*-
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = len(coins)+1
        n = amount+1

        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m):
            for j in range(1, n):
                if coins[i-1] > j or dp[i][j-coins[i]] == float('inf'):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-coins[i-1]]+1)
        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]