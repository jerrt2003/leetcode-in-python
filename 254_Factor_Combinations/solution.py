from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.ret: List[List[int]] = []
        path = []
        self.target = n
        self.dfs(2, n, path)
        return self.ret

    def dfs(self, curr:int, n: int, path: List[int]) -> None:
        if n == 1 and path:
            self.ret.append(path)
        for i in range(curr, n+1):
            if n % i != 0 or i == self.target:
                continue
            self.dfs(i, n//i, path + [i])