from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        return self._findPeakElement(l, r, nums)
    

    def _findPeakElement(self, l: int, r: int, nums: List[int]) -> int:
        if l == r:
            return l
        m = (l+r)//2
        if nums[m] > nums[m+1]:
            return self._findPeakElement(l, m, nums)
        else:
            return self._findPeakElement(m+1, r, nums)