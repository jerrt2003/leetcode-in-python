# -*- coding: utf-8 -*-
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        DP = [[[0,0] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    DP[i][j] = grid[i][j]
                    continue
                if i == 0:
                    DP[i][j] = DP[i][j-1] + grid[i][j]
                    continue
                if j == 0:
                    DP[i][j] = -(abs(DP[i-1][j]) + grid[i][j])
                    continue
                if abs(DP[i-1][j]) < abs(DP[i][j-1]):
                    DP[i][j] = -(abs(DP[i-1][j]) + grid[i][j])
                else:
                    DP[i][j] = abs(DP[i][j-1]) + grid[i][j]
        i = m-1
        j = n-1
        path = []
        while i > -1 and j > -1:
            path.append((i, j))
            if DP[i][j] < 0:
                i -= 1
            else:
                j -= 1

        path.reverse()
        return path


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print Solution().minPathSum(grid)