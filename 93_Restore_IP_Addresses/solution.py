from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []
        self.dfs(path, s, 0, ans)
        return ans
        

    def dfs(self, path: List[str], s: str, idx: int, ans: List[str]):
        # DFS終止條件
        if idx == len(s):
            if len(path) == 4:
                ans.append(".".join(path))
            return
        # 剪枝1：假設區塊已經填滿，但是還沒有遍歷完整個字串，則直接返回
        if len(path) == 4 and idx < len(s):
            return
        for i in range(idx, len(s)):
            # 剪枝2：如果區塊長度大於1且第一個數字是0，就不用繼續往下遍歷了，因為0只能單獨成為一個區塊
            if len(s[idx:i+1]) > 1 and s[idx] == "0":
                break
            if int(s[idx:i+1]) <= 255:
                self.dfs(path+[s[idx:i+1]], s, i+1, ans)