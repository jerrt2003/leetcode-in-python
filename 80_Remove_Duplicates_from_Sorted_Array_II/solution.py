from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self._removeAtMostK(nums, 2)

    def _removeAtMostK(self, nums: List[int], k: int) -> int:
        idx = 0 # point to the last position which suppose to be replaced
        for num in nums:
            if k > idx or num != nums[idx-k]:
                nums[idx] = num
                idx += 1
        return idx