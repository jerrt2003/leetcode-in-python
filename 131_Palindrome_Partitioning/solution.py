from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        path = []
        self.dfs(s, 0, path)
        return self.ans

    def dfs(self, s: str, idx: int, path: List[str]):
        if idx == len(s):
            self.ans.append(path)
            return

        for i in range(idx, len(s)):
            if s[idx : i + 1] == s[idx : i + 1][::-1]:
                self.dfs(s, i + 1, path + [s[idx : i + 1]])
