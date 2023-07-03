from typing import List


class Solution:
    # 失敗的Meomization:
    # 在這裡我們使用了一個self.can_break的list來記錄每個sum是否可以被break
    # 當我們在dfs的過程中發現某個sum不能被break時，我們就可以直接return False
    # 可是這個假設是錯誤的：
    # 首先，我們用了一個排列過的數列 也就是說當我們在dfs的過程中，我們不會"回頭"使用之前的數字
    # 但是在這樣個做法下，我們會錯過一些可能的解
    # ex. [1,3,9] 8 -> 在這個情況下假設我們遍歷到[1,3], 接下來只能使用 9, 但很明顯 1+3+9 == 13 > 8, 所以我們會說當1+3==4時，我們不能break
    # 但實際上這是錯誤的 因為我們可以使用 1+3+1+1+1+1 == 8 <- 所以這個情況下我們不能說 1+3==4時不能break
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = sorted(coins)
        self.amount = amount
        self.ans = float("inf")
        self.can_break = [True for _ in range(amount + 1)]

        self.dfs(0, 0, 0)

        return -1 if self.ans == float("inf") else self.ans

    def dfs(self, cur_coins_counter: int, cur_sum: int, idx: int) -> bool:
        if cur_sum == self.amount:
            self.ans = min(self.ans, cur_coins_counter)
            return True

        if not self.can_break[cur_sum]:
            return False

        can_break = False
        for i in range(idx, len(self.coins)):
            if cur_sum + self.coins[i] > self.amount:
                break
            if self.dfs(cur_coins_counter + 1, cur_sum + self.coins[i], i):
                can_break = True

        self.can_break[cur_sum] = can_break
        return self.can_break[cur_sum]
