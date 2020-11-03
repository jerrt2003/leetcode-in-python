class Solution(object):
    def largestIsland(self, grid):
        """
        Facebook
        DFS
        T:O(mn) S:O(mn)
        Runtime: 136 ms, faster than 57.60% of Python online submissions for Making A Large Island.
        Memory Usage: 14.5 MB, less than 38.46% of Python online submissions for Making A Large Island.
        :type grid: List[List[int]]
        :rtype: int
        """
        island = dict()
        m, n = len(grid), len(grid[0])

        def dfs(i, j, idx):
            area = 1
            grid[i][j] = idx
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    area += dfs(x, y, idx)
            return area

        idx = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, idx)
                    island[idx] = area
                    idx += 1

        ans = -float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    connect_island = set()
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                            connect_island.add(grid[x][y])
                    ans = max(ans, sum(island[idx] for idx in list(connect_island)) + 1)

        return m*n if ans == -float('inf') else ans


print Solution().largestIsland([[1, 0], [0, 1]])
print Solution().largestIsland([[1,0,1,0,1],[1,1,0,1,1],[0,1,0,0,1]])
print Solution().largestIsland([[1]])