class Solution(object):
    def minPathSum(self, grid):
        """
        DP Solution: Similar to Problem 62: https://leetcode.com/problems/unique-paths/description/
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                    continue
                if j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                    continue
                grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

sol = Solution()
print sol.minPathSum(grid)