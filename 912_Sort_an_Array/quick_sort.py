import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1
        self._quick_sort(low, high, nums)
        return nums
        
    def _quick_sort(self, low: int, high: int, nums: List[int]) -> None:
        # 遞歸返回條件
        if low >= high:
            return
        mid = self._partition(low, high, nums)
        self._quick_sort(low, mid-1, nums)
        self._quick_sort(mid+1, high, nums)

    def _partition(self, low: int, high: int, nums: List[int]) -> int:
        # 選取pivot_idx
        pivot_idx = random.randint(low, high)
        # 將pivot換到首位(因為pivot已知 相當於把首位空下來)
        nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
        pivot = nums[low]
        l, r = low, high
        while l < r:
            # r由右往左移動 找到一個小於pivot的數 將其挪到'空出來'的位置(此時的 l)
            # 完成'挪動'後此時 r 相當於也空了下來
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            # l由左往右移動 找到一個大於pivot的數 將其挪到'空出來'的位置(此時的 r)
            # 完成'挪動'後此時 l 相當於也空了下來
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l