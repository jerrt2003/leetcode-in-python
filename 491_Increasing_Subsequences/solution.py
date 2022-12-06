from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ret: List[List[int]] = []
        self.helper(0, [], nums)
        return self.ret

    def helper(self, idx: int, path: List[int], nums: List[int]):
        if idx == len(nums):
            return
        if len(path) > 1:
            self.ret.append(path)
        used = set()
        for i in range(idx, len(nums)):
            if nums[i] in used:
                continue
            if len(path) > 0 and nums[i] < path[-1]:
                continue
            used.add(nums[i])
            self.helper(i+1, path + [nums[i]], nums)
