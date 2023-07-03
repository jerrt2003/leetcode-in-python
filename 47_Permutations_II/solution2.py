from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        path = []
        self.dfs(sorted(nums), path)

        return self.ans

    def dfs(self, nums: List[int], path: List[int]):
        if not nums:
            self.ans.append(path)

        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            self.dfs(nums[:i] + nums[i + 1 :], path + [nums[i]])
