from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        path = []
        self.dfs(path, nums)
        return self.ans

    def dfs(self, path: List[int], nums: List[int]):
        if not nums:
            self.ans.append(path)
            return

        for i in range(0, len(nums)):
            self.dfs(path + [nums[i]], nums[:i] + nums[i + 1 :])
