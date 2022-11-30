from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # check rotten orange pos and place into queue (i.e. init q)
        # count all oranges
        m, n = len(grid), len(grid[0])
        total_count = 0
        rotten_count = 0
        q: List[List[int]] = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    total_count += 1
                    if grid[i][j] == 2:
                        rotten_count += 1
                        q.append([i, j])
                    
        # BFS
        # if node is not visited, mark it and push into queue
        # increase level by 1
        level = 0
        while q:
            level_len = len(q)
            for _ in range(level_len):
                cords = q.pop(0)
                for x, y in [[1, 0],[-1, 0],[0, 1],[0, -1]]:
                    i, j = cords[0], cords[1]
                    i += x
                    j += y
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        rotten_count += 1
                        q.append([i, j])
            level += 1
        return level-1 if total_count == rotten_count else -1