# -*- coding: utf-8 -*-
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        Perf: Runtime: 628 ms, faster than 90.15% / Memory Usage: 22.2 MB, less than 56.60%
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            ret = 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                ret += dfs(x, y)
            return ret

        def isConnected(i, j):
            if i == 0:
                return True
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 2:
                    return True
            return False

        for i, j in hits:
            grid[i][j] -= 1

        for j in range(n):
            dfs(0, j)

        res = [0] * len(hits)
        for idx in range(len(hits) - 1, -1, -1):
            i, j = hits[idx]
            grid[i][j] += 1
            if grid[i][j] == 1 and isConnected(i, j):
                res[idx] = dfs(i, j) - 1
        return res