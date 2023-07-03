# 對於這個問題，我們可以使用動態規劃來實現，並且使用了儲存以前結果的想法，這種儲存以前結果的方法也被稱為記憶化。以下是改進後的代碼：
# 在這個版本中，我們不再使用DFS搜索所有可能的解，而是使用動態規劃。`dp[i]`是當前金額為`i`時所需的最少硬幣數量。我們將其初始值設為無窮大，表示我們還沒有找到組成該金額的方法。
# 對於每一種硬幣，我們從該硬幣的面值開始遍歷到`amount`，並將`dp[x]`更新為`min(dp[x], dp[x - coin] + 1)`。這表示要組成金額`x`，我們可以不使用這個硬幣（即保持原狀），或者使用這個硬幣（即從`dp[x - coin]`的基礎上加一）。
# 最後，如果`dp[amount]`仍然是無窮大，則表示無法用這些硬幣組成`amount`，我們返回-1；否則，我們返回`dp[amount]`。
# 這個方法的時間複雜度為`O(amount * len(coins))`，空間複雜度為`O(amount)`，其中`amount`是給定的金額，`coins`是硬幣的面值列表。


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [float("inf") for _ in range(amount + 1)]
        DP[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                DP[x] = min(DP[x], DP[x - coin] + 1)

        return DP[amount] if DP[amount] != float("inf") else -1
