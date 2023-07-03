from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        cur_path = []
        self.s = s

        self.dfs(cur_path, 0)

        return self.ans

    def dfs(self, cur_path: List[int], idx: int):
        if len(cur_path) == 4:
            if idx == len(self.s):
                self.ans.append(".".join(cur_path))
            return

        if len(cur_path) == 4 and idx < len(self.s):
            return

        for i in range(idx, len(self.s)):
            ip = self.s[idx : i + 1]
            if len(ip) > 1 and self.s[idx] == "0":
                break
            if int(ip) > 255:
                break
            self.dfs(cur_path + [ip], i + 1)
