# -*- coding: utf-8 -*-
class Solution(object):
    def numIslands(self, grid):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - A DFS solution
        - Mark visited Node as 'x' (if it is an island '1')
        :type grid: List[List[str]]
        :rtype: int
        """
        self.res = 0
        self.grid = grid
        if self.grid is None or len(self.grid) == 0:
            return 0
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if self.findIsland(i, j):
                    self.res += 1
        return self.res


    def findIsland(self, i, j):
        if self.grid[i][j] == '0' or self.grid[i][j] == 'x': # if visited or the node is ocean, just stop searching (return)
            return False
        self.grid[i][j] = 'x'
        if i > 0:
            self.findIsland(i-1, j)
        if i < self.row-1:
            self.findIsland(i+1, j)
        if j > 0:
            self.findIsland(i, j-1)
        if j < self.col-1:
            self.findIsland(i, j+1)
        return True
'''
grid = [['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']]
'''
grid = []


sol = Solution()
print sol.numIslands(grid)