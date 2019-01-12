# -*- coding: utf-8 -*-
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        Solution: BFS
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: MySELF!!
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        self.grid = grid

        def BFS(i, j):
            stack = [(i, j)]
            directions = [(1, 0),(0, 1),(-1, 0),(0, -1)]
            area = 0
            while stack:
                x, y = stack.pop(0)
                area += 1
                self.grid[x][y] = 'x'
                for x_dir, y_dir in directions:
                    p, q = x + x_dir, y + y_dir
                    if 0 <= p < len(grid) and 0 <= q < len(grid[0]) and self.grid[p][q] == 1 and (p, q) not in stack:
                        stack.append((p, q))
            self.res = max(self.res, area)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1:
                    BFS(i, j)

        return self.res

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
print Solution().maxAreaOfIsland(grid)