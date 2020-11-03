class Solution(object):
    def uniquePathsIII(self, grid):
        """
        Backtracking Brutal Force
        T:O(4^RC) S:O(RC)
        Runtime: 36 ms, faster than 94.55% of Python online submissions for Unique Paths III.
        Memory Usage: 12.7 MB, less than 82.16% of Python online submissions for Unique Paths III.
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 1
        self.ans = 0
        start, end = [0, 0], [0, 0]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    start[0], start[1] = i, j
                elif grid[i][j] == 2:
                    end[0], end[1] = i, j

        def dfs(i, j, count, grid):
            if grid[i][j] == 2:
                if count == 0:
                    self.ans += 1
                return
            c = grid[i][j]
            grid[i][j] = -1
            for x, y in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    dfs(x, y, count-1, grid)
            grid[i][j] = c

        dfs(start[0],start[1],count, grid)
        return self.ans

print Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
print Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
print Solution().uniquePathsIII([[0,1],[2,0]])