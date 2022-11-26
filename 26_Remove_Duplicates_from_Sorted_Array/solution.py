from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        j :int = 0
        for i in range(0, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j+1