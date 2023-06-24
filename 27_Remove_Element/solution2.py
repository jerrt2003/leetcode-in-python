from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return idx
