# -*- coding: utf-8 -*-
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        UF = [-1 for _ in range(m*n)]

        def findRoot(root):
            while root != UF[root]:
                root = UF[UF[root]]
            return root

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    root = i * n + j
                    UF[root] = root
                    for x_dir, y_dir in directions:
                        x = i + x_dir
                        y = j + y_dir
                        neighbor = x * n + y
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0' or UF[neighbor] == -1:
                            continue
                        neighborRoot = findRoot(neighbor)
                        if neighborRoot != root:
                            UF[root] = neighborRoot
                            root = neighborRoot
                            count -= 1
        return count


grid = ['11110','11010','11000','00000']
print Solution().numIslands(grid)