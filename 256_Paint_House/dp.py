from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        num_houses = len(costs)
        num_colors = len(costs[0])
        dp = [[float('inf')]*3 for _ in range(num_houses)]
        # 定义dp[i][j]为将第 i 间房子粉刷为颜色 j 时的最小花费。
        # 因为相邻的房子颜色不能相同，那么当前房子的最小花费就与前面房子的颜色有关，
        # 当前房子能选的颜色有三种，而每一种颜色都结果由前面房子涂其他两种颜色的结果决定
        # 初始化即为第一间房子涂三种颜色的花费
        # 塗第0間房子
        for i in range(num_colors):
            dp[0][i] = costs[0][i]

        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[num_houses-1])