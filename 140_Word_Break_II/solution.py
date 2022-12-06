from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ret: List[str] = []
        path: List[str] = []
        self.helper(0, path, s, wordDict)
        return self.ret

    def helper(self, idx: int, path: List[str], s: str, wordDict: List[str]) -> None:
        if idx == len(s):
            self.ret.append(" ".join(path))
            return
        for i in range(idx, len(s)):
            if s[idx:i+1] in wordDict:
                self.helper(i+1, path + [s[idx:i+1]], s, wordDict)
