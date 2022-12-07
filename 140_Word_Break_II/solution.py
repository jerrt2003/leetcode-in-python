from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ret: List[str] = []
        path: List[str] = []
        # create a list to record if s[i:] can be break or not
        self.memo = [1 for _ in range(len(s))]
        self.can_break = [0 for _ in range(len(s))]
        self.helper(0, path, s, wordDict)
        return self.ret

    def helper(self, idx: int, path: List[str], s: str, wordDict: List[str]) -> None:
        ans_count = len(self.ret)
        if idx == len(s):
            self.ret.append(" ".join(path))
            return
        for i in range(idx, len(s)):
            # 假設self.memo[i]為0 表示s[i+1:]的字串無法break 不需要往下DFS == 剪枝
            if s[idx:i+1] in wordDict and self.memo[i]:
                self.helper(i+1, path + [s[idx:i+1]], s, wordDict)
            if len(self.ret) == ans_count:
                self.memo[i] == 0