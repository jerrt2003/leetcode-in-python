from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        target = nums_sum // k
        return self.dfs(0, k, target, sorted(nums, reverse=True))

    def dfs(self, path_sum, k, target, nums) -> bool:
        if len(nums) == 0:
            if k == 0:
                return True
            return False
        for i in range(len(nums)):
            if path_sum + nums[i] > target:
                continue
            elif path_sum + nums[i] == target:
                if self.dfs(0, k - 1, target, nums[:i] + nums[i + 1 :]):
                    return True
            else:
                if self.dfs(path_sum + nums[i], k, target, nums[:i] + nums[i + 1 :]):
                    return True
