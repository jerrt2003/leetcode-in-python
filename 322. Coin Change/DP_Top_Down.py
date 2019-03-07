# -*- coding: utf-8 -*-
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        DP:
        Time Complexity:
        Space Complexity:
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # sort coins (from big to small)
        # DP[amount] ==> ans for amount
        # DP[amount] = min(DP[amount], find_min(amount-coin)+1)
        #coins.sort(reverse=True)
        DP = [sys.maxint for _ in range(amount+1)]

        def findMin(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if DP[amount] != sys.maxint:
                return DP[amount]
            for coin in coins:
                if coin > amount:
                    continue
                elif coin <= amount:
                    tmp = findMin(amount-coin)
                    if tmp == -1:
                        continue
                    else:
                        DP[amount] = min(DP[amount], tmp+1)
            if DP[amount] == sys.maxint:
                return -1
            return DP[amount]

        return findMin(amount)

coins = [1,2,5]
amount = 11
sol = Solution()
print sol.coinChange(coins, amount)


#coins = [186,419,83,408]
#amount = 6249
# ans = 20

coins = [1,2,5]
amount = 11
sol = Solution()
print sol.coinChange(coins, amount)