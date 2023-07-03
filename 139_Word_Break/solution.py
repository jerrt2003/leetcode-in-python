from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        self.s = s
        self.canBreak = [True for _ in range(len(self.s))]
        return self.dfs(0)

    def dfs(self, idx: int) -> bool:
        if idx == len(self.s):
            return True

        if not self.canBreak[idx]:
            return False

        for i in range(idx, len(self.s)):
            if self.s[idx : i + 1] in self.wordDict:
                if self.dfs(i + 1):
                    return True

        self.canBreak[idx] = False

        return False
