from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        self.s = s
        self.wordDict = set(wordDict)
        self.canBreak = [True for _ in range(len(self.s))]

        self.dfs(0, [])

        return self.ans

    def dfs(self, idx: int, path: List[str]) -> bool:
        if idx == len(self.s):
            self.ans.append(" ".join(path))
            return True

        if not self.canBreak[idx]:
            return False

        canBreakAtIdx = False
        for i in range(idx, len(self.s)):
            if self.s[idx : i + 1] in self.wordDict:
                if self.dfs(i + 1, path + [self.s[idx : i + 1]]):
                    canBreakAtIdx = True

        self.canBreak[idx] = canBreakAtIdx
        return canBreakAtIdx
