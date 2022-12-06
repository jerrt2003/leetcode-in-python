from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return self.dfs(n)
        return self.bfs(n)

    # dfs
    def dfs(self, n: int) -> List[str]:
        self.ret: List[str] = []
        self.helper(n, n, [])
        return self.ret

    def helper(self, l: int, r: int, path: List[str]) -> None:
        if l == 0 and r == 0:
            self.ret.append("".join(path))
            return
        if l > r: 
            return
        # 選l的情況            
        if l > 0:
            self.helper(l-1, r, path + ["("])
        # 選r的情況
        if r > 0:
            self.helper(l, r-1, path + [")"])

    def bfs(self, n: int) -> List[str]:
        ret: List[int] = []
        q: List[List[any]] = []
        q.append([n, n, []])
        while q:
            l, r, path = q.pop(0)
            if l == 0 and r == 0:
                ret.append("".join(path))
                continue
            if l > r:
                continue
            if l > 0:
                q.append([l-1, r, path + ["("]])
            if r > 0:
                q.append([l, r-1, path + [")"]])
        return ret
