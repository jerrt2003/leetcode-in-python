class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j, visit):
            visit.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visit:
                    dfs(x, y, visit)

        ans = -float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visit = set()
                    dfs(i, j, visit)
                    ans = max(ans, len(list(visit)))
        return ans

# print Solution().largestIsland([[1,0],[0,1]])
print Solution().largestIsland([[1,0,1,0,1],[1,1,0,1,1],[0,1,0,0,1]])