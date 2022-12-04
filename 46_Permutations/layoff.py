from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret: List[List[int]] = []
        self.helper(nums, [])
        return self.ret

    def helper(self, nums: List[int], path: List[int]) -> None:
        if not nums:
            self.ret.append(path)
            return
        for i, v in enumerate(nums):
            self.helper(nums[:i]+nums[i+1:], path + [v])