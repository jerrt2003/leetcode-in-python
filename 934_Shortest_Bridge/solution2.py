import collections
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.q = collections.deque([])
        self.m, self.n = len(grid), len(grid[0])
        found_island = False
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 and not found_island:
                    self.grid[i][j] = 2
                    self.q.append((i, j))
                    self.find_island(i, j)
                    # 找到島嶼後，將 found_island 設為 True，並跳出雙層迴圈。
                    found_island = True

        ans = 0
        while self.q:
            q_len = len(self.q)
            for _ in range(q_len):
                i, j = self.q.popleft()
                for diff_i, diff_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x, y = i + diff_i, j + diff_j
                    if 0 <= x and x < self.m and 0 <= y and y < self.n:
                        if self.grid[x][y] == 1:
                            return ans
                        elif self.grid[x][y] == 0:
                            self.grid[x][y] = 2
                            self.q.append((x, y))
            # 每次 BFS 循環完成後，將橋樑長度 ans 增加1。(搭橋完成)
            ans += 1

        return -1

    def find_island(self, i: int, j: int) -> None:
        for diff_i, diff_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = i + diff_i
            y = j + diff_j
            if 0 <= x and x < self.m and 0 <= y and y < self.n and self.grid[x][y] == 1:
                self.grid[x][y] = 2
                self.q.append((x, y))
                self.find_island(x, y)
