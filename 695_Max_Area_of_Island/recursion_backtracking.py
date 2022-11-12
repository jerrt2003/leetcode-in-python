# -*- coding: utf-8 -*-
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/max-area-of-island/discuss/108541/easy-python
        TP:
        - DFS
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.col = len(grid)
        self.row = len(grid[0])
        area = max([self.dfs(i, j) for i in range(self.col) for j in range(self.row)])
        return area if area else 0


    def dfs(self, i, j):
        if 0 <= i < self.col and 0 <= j < self.row and self.grid[i][j] == 1:
            self.grid[i][j] = 0
            return 1 + self.dfs(i-1, j) + self.dfs(i+1, j) + self.dfs(i, j-1) + self.dfs(i, j+1)
        return 0


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]


'''
grid = [[1,0,1],
        [1,1,1],
        [0,0,1]]
'''

sol = Solution()
print sol.maxAreaOfIsland(grid)