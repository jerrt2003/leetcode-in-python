from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l, r = n, n
        self.ans = []

        self.dfs(l, r, [])

        return self.ans

    def dfs(self, l: int, r: int, path: List[str]):
        if l == 0 and r == 0:
            self.ans.append("".join(path))
            return

        if l > r:
            return
        if l > 0:
            self.dfs(l - 1, r, path + ["("])
        if r > 0:
            self.dfs(l, r - 1, path + [")"])
