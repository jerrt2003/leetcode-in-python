# -*- coding: utf-8 -*-
class Solution(object):
    def coinChange(self, coins, amount):
        """
        Solution: DP + Early Termination
        Time Complexity:
        Space Complexity: O(1)
        Perf: Runtime: 192 ms, faster than 96.72% / Memory Usage: 10.9 MB, less than 84.94%
        Inspired By: https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up
        TP:
        - Basically using from largest coins possible and using DP to dig out possible combination
        - Terminate the DFS when it will definitely exceeds current min level
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        self.coins = coins
        self.len_coins = len(coins)
        self.res = float('inf')

        def dfs(remain, level, idx):
            if remain == 0:
                self.res = min(self.res, level)
                return
            else:
                for i in range(idx, self.len_coins):
                    if self.coins[i] <= remain < self.coins[i]*(self.res - level):
                        dfs(remain - self.coins[i], level+1, i)
            return

        for i in range(self.len_coins):
            dfs(amount, 0, i)
        return -1 if self.res == float('inf') else self.res

coins = [1,2,5]
amount = 100

print Solution().coinChange(coins, amount)