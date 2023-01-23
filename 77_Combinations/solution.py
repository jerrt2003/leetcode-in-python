from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret: List[List[int]] = []
        self.helper(1, n, k, [])
        return self.ret
    
    def helper(self, start: int, n: int, k: int, path: List[int]) -> None:
        if len(path) == k:
            self.ret.append(path)
            return
        # 剪枝
        if len(path) + (n-start+1) < k:
            return
        for i in range(start, n+1):
            self.helper(i+1, n, k, path + [i])
        