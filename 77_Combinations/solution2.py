from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.nums = [i + 1 for i in range(n)]
        self.k = k
        idx = 0
        path = []
        self.dfs(idx, path)

        return self.ans

    def dfs(self, idx: int, path: List[int]):
        if len(path) == self.k:
            self.ans.append(path)
            return

        for i in range(idx, len(self.nums)):
            if len(path) + len(self.nums) - i + 1 < self.k:
                break
            self.dfs(i + 1, path + [self.nums[i]])
