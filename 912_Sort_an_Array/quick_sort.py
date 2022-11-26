import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1
        self._quick_sort(low, high, nums)
        return nums
        
    def _quick_sort(self, low: int, high: int, nums: List[int]) -> None:
        if low >= high:
            return
        mid = self._partition(low, high, nums)
        self._quick_sort(low, mid-1, nums)
        self._quick_sort(mid+1, high, nums)

    def _partition(self, low: int, high: int, nums: List[int]) -> int:
        pivot_idx = random.randint(low, high)
        nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
        pivot = nums[low]
        l, r = low, high
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l