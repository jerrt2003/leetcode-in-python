from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums)
        while l < r:
            m = (l+r-1)//2
            if nums[m] >= target:
                r = m
            else:
                l = m+1
        return l
