from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        cur_path = []

        self.dfs(cur_path, 0)

        return self.ans

    def dfs(self, cur_path: List[int], idx) -> None:
        if idx == len(self.nums):
            return

        visited = set()
        for i in range(idx, len(self.nums)):
            if self.nums[i] in visited:
                continue
            visited.add(self.nums[i])
            if len(cur_path) > 0 and self.nums[i] < cur_path[-1]:
                continue
            if len(cur_path + [self.nums[i]]) > 1:
                self.ans.append(cur_path + [self.nums[i]])
            self.dfs(cur_path + [self.nums[i]], i + 1)
