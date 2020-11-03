class Solution(object):
    def minCost(self, grid):
        """
        DFS
        T:O(4^mn) S:O(1)
        TLE
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        self.min_cost = float('inf')
        self.grid = grid
        def dfs(i, j, cost):
            if (i, j) == (m-1, n-1):
                self.min_cost = min(self.min_cost, cost)
                return
            org = self.grid[i][j]
            self.grid[i][j] = -1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and self.grid[x][y] != -1:
                    if ((x, y) == (i-1, j) and org != 4) or ((x, y) == (i+1, j) and org != 3) or ((x, y) == (i, j-1) and org != 2) or ((x, y) == (i, j+1) and org != 1):
                        dfs(x, y, cost+1)
                    else:
                        dfs(x, y, cost)
            self.grid[i][j] = org

        dfs(0, 0, 0)
        return self.min_cost

print Solution().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])
print Solution().minCost([[1,1,3],[3,2,2],[1,1,4]])
