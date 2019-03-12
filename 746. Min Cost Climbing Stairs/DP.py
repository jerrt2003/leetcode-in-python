# -*- coding: utf-8 -*-
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 24 ms, faster than 98.40% / Memory Usage: 11 MB, less than 7.86%
        Inspired By: MySELF!!
        :type cost: List[int]
        :rtype: int
        """
        m = len(cost)
        DP = [0 for _ in range(m)]
        DP[0] = 0
        DP[1] = 0
        for i in range(2, m):
            DP[i] = min(DP[i - 2] + cost[i - 2], DP[i - 1] + cost[i - 1])
        return min(DP[-1] + cost[-1], DP[-2] + cost[-2])

