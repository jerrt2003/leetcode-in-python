from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        path: List[str] = []
        self.ans = 0
        self.n = n
        self.dfs(path, 0)

        return self.ans

    def dfs(self, path: List[str], row_idx: int):
        if row_idx == self.n:
            self.ans += 1
            return

        for i in range(self.n):
            if self.is_valid_placement(path, row_idx, i):
                next_placement = ""
                for j in range(self.n):
                    if j == i:
                        next_placement += "Q"
                    else:
                        next_placement += "."
                self.dfs(path + [next_placement], row_idx + 1)

    def is_valid_placement(self, path: List[str], x: int, y: int) -> bool:
        for i in range(len(path)):
            if path[i][y] == "Q":
                return False

        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            if path[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = x - 1, y + 1
        while i >= 0 and j < self.n:
            if path[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True
