from typing import List, Set


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        return len(nums) > 6 and any(
            self.dfs(nums[:i]) & self.dfs(nums[i + 1 :])
            for i in range(3, len(nums) - 3)
        )

    def dfs(self, nums: List[int]) -> Set[int]:
        total = sum(nums)
        prefix_sum = [0 for _ in range(len(nums))]
        cur_sum = 0
        for i in range(0, len(nums)):
            cur_sum += nums[i]
            prefix_sum[i] = cur_sum
        return {
            prefix_sum[i - 1]
            for i in range(1, len(nums))
            if total - prefix_sum[i] == prefix_sum[i - 1]
        }
