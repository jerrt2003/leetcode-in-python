class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        DP = [0] * (amount+1)
        DP[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                DP[i] += DP[i-coin]
        return DP[-1]

amount = 5
coins = [1, 2, 5]
assert Solution().change(amount, coins) == 4