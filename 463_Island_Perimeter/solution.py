import collections
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    q.append([i, j])
                    break
        ans = 0
        while q:
            i, j = q.popleft()
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x and x < m and 0 <= y and y < n:
                    if grid[x][y] == 1:
                        q.append([x, y])
                        grid[x][y] = -1
                    elif grid[x][y] == 0:
                        ans += 1
                else:
                    ans += 1

        return ans
