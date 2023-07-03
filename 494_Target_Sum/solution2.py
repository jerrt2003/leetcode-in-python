import collections
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        self.ans = 0
        self.DP = collections.defaultdict(int)

        return self.dfs(0, 0)

    def dfs(self, cur_idx: int, cur_sum: int) -> int:
        if (cur_idx, cur_sum) in self.DP.keys():
            return self.DP[(cur_idx, cur_sum)]

        if cur_idx == len(self.nums):
            self.DP[(cur_idx, cur_sum)] = 1
            return self.DP[(cur_idx, cur_sum)]

        self.DP[(cur_idx, cur_sum)] = self.dfs(
            cur_idx + 1, cur_sum + self.nums[cur_idx]
        ) + self.dfs(cur_idx + 1, cur_sum - self.nums[cur_idx])

        return self.DP[(cur_idx, cur_sum)]
