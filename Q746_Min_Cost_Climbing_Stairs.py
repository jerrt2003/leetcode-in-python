class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = list()
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        return min(dp[len(cost)-1], dp[len(cost)-2])

a = [10, 15, 20]
b = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sol = Solution()
print sol.minCostClimbingStairs(b)
