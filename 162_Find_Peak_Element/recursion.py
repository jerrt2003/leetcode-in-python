from typing import List

class Solution:
    """
    Recursion method will generate the peak element of "WHOLE ARRAY"
    """
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        return self._find_peak_element(l, r, nums)
    

    def _find_peak_element(self, l: int, r: int, nums: List[int]) -> int:
        if l == r:
            return l
        m = (l+r)//2
        left_idx = self._find_peak_element(l, m, nums)
        right_idx = self._find_peak_element(m+1, r, nums)
        if nums[left_idx] >= nums[right_idx]:
            return left_idx
        else:
            return right_idx