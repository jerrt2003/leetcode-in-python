# -*- coding: utf-8 -*-
class Solution(object):
    def minPathSum(self, grid):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        Inspired By: MySELF!! (48ms, beat 97.84%)
        TP:
        - faster than Dijkestra
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for j in range(1, n):
            grid[0][j] = grid[0][j - 1] + grid[0][j]
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

