from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = sorted(coins)
        self.amount = amount
        self.ans = float("inf")

        self.dfs(0, 0, 0)

        return self.ans

    def dfs(self, cur_coins_counter: int, cur_sum: int, idx: int) -> bool:
        if cur_sum == self.amount:
            self.ans = min(self.ans, cur_coins_counter)
            return

        for i in range(idx, len(self.coins)):
            if cur_sum + self.coins[i] > self.amount:
                break
            self.dfs(cur_coins_counter + 1, cur_sum + self.coins[i], i)
