# -*- coding: utf-8 -*-
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        Solution: DFS
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: MySELF!!
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0

        def findMaxIsland(i, j, grid):
            grid[i][j] = 'x'
            self.area += 1
            self.res = max(self.res, self.area)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x_dir, y_dir in directions:
                x, y = i + x_dir, j + y_dir
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'x' and grid[x][y] == 1:
                    findMaxIsland(x, y, grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 'x' and grid[i][j] == 1:
                    self.area = 0
                    findMaxIsland(i, j, grid)
        return self.res

grid = [[1,1],[1,0]]
print Solution().maxAreaOfIsland(grid)