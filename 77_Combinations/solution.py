from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ret: List[List[int]] = []
        self.helper(1, n, k, [])
        return self.ret
    
    def helper(self, start: int, n: int, k: int, path: List[int]) -> None:
        if len(path + [start]) == k:
            self.ret.append(path + [start])
            return
        if n - start + len(path+[start]) < k:
            return
        for i in range(start+1, n+1):
            self.helper(i, n, k, path + [start])
        for i in range(start+1, n+1):
            self.helper(i, n, k, [start])            
        