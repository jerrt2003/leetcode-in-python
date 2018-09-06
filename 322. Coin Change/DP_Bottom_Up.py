class Solution(object):
    def coinChange(self, coins, amount):
        """
        DP Top-Bottom: 從amount=0開始找DP
        Space Complexity:
        Time Complexity:
        Inspired By: https://leetcode.com/problems/coin-change/discuss/77360/C++-O(n*amount)-time-O(amount)-space-DP-solution
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        DP = [float('inf') for _ in range(amount+1)]
        DP[0] = 0 # amount=0 的話其DP[i]=0
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    DP[i] = min(DP[i], DP[i-coin]+1) # 回頭找DP[i-coin], 萬一DP[i-coin]沒有,其數值會是float('inf')所以最後的DP[i]也會是float('inf')
        if DP[amount] == float('inf'):
            return -1
        else:
            return DP[amount]

#coins = [186,419,83,408]
#amount = 6249
#ans = 20

coins = [474,83,404,3]
amount = 264
# ans = 8

#coins = [3]
#amount = 2

sol = Solution()
print sol.coinChange(coins, amount)