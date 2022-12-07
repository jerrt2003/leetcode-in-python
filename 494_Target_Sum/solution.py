from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        path: List[int] = []
        self.helper(0, path, nums, target)
        return self.count

    def helper(self, idx: int, path: List[int], nums: List[int], target: int) -> None:
        if idx == len(nums):
            if sum(path) == target:
                self.count += 1
                return
        self.helper(idx+1, path + [1 * nums[idx]], nums, target)
        self.helper(idx+1, path + [-1 * nums[idx]], nums, target)

