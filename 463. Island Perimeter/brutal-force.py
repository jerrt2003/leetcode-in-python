class Solution(object):
    def islandPerimeter(self, grid):
        """
        T:O(4mn) S:O(1)
        Runtime: 584 ms, faster than 65.57% of Python online submissions for Island Perimeter.
        Memory Usage: 12.9 MB, less than 85.59% of Python online submissions for Island Perimeter.
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def check(i, j):
            ans = 4
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    ans -= 1
            return ans

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += check(i, j)
        return ans



