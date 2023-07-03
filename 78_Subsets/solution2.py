from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        self.nums = nums
        path = []
        self.dfs(0, path)

        return self.ans

    def dfs(self, idx, path):
        if idx == len(self.nums):
            return

        for i in range(idx, len(self.nums)):
            self.ans.append(path + [self.nums[i]])
            self.dfs(i + 1, path + [self.nums[i]])
