# -*- coding: utf-8 -*-
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: MySELF!!
        Perf: Runtime: 24 ms, faster than 45.28% / Memory Usage: 10.8 MB, less than 42.86%
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        DP = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = 0
                elif i == 0 and j == 0:
                    DP[i][j] = 1
                elif i == 0:
                    DP[0][j] = DP[0][j-1]
                elif j == 0:
                    DP[i][0] = DP[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if DP[i][j] == float('inf'):
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[-1][-1]