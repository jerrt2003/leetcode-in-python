class Solution(object):
    def getMaximumGold(self, grid):
        """
        T:O(4*3^k) S:O(k)

        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j, cost):
            if (i, j) in self.seen:
                return
            self.seen.add((i, j))
            dp[i][j] = max(dp[i][j], cost+grid[i][j])
            for (x, y) in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                if 0<=x<m and 0<=y<n and grid[x][y] and (x, y) not in self.seen:
                    dfs(x, y, cost+grid[i][j])
            self.seen.remove((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.seen = set()
                    dfs(i, j, 0)

        return max(c for row in dp for c in row)

print Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])
print Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])