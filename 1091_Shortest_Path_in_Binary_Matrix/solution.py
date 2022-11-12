class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        T:O(mn) S:O(mn)
        Runtime: 564 ms, faster than 76.64% of Python online submissions for Shortest Path in Binary Matrix.
        Memory Usage: 12.9 MB, less than 95.18% of Python online submissions for Shortest Path in Binary Matrix.
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        q = [(0, 0)]
        grid[0][0] = -1
        count = 1
        while q:
            l = len(q)
            for _ in range(l):
                i, j = q.pop(0)
                if i == m-1 and j == n-1:
                    return count
                for x, y in [(i-1, j-1),(i-1, j),(i-1, j+1),(i, j-1),(i, j+1),(i+1, j-1),(i+1, j),(i+1, j+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = -1
                        q.append((x, y))
            count += 1
        return -1

print Solution().shortestPathBinaryMatrix([[0,1],[1,0]])
print Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])