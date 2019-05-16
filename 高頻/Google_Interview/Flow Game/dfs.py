# -*- coding: utf-8 -*-
"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=521017&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3086%5D%5Bvalue%5D%3D9%26searchoption%5B3086%5D%5Btype%5D%3Dradio%26searchoption%5B3089%5D%5Bvalue%5D%5B2%5D%3D2%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26searchoption%5B3109%5D%5Bvalue%5D%3D2%26searchoption%5B3109%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
"""

class Solution(object):
    def goPath(self, grid):
        self.grid = grid
        self.visited = set()
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j, grid[i][j])
        return self.grid

    def dfs(self, i, j, color):
        if (i, j) in self.visited:
            return
        self.grid[i][j] = -1*color
        self.visited.add((i, j))
        for delta_x, delta_y in [(1,0),(0,1),(-1,0),(0,-1)]:
            x, y = i+delta_x, j+delta_y
            if 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] == color:
                self.dfs(x, y, color)
        return


grid = [[1,1,1,1,4],
        [1,3,4,4,4],
        [1,3,2,2,2],
        [1,3,2,5,2],
        [2,2,2,5,5]]

print Solution().goPath(grid)
