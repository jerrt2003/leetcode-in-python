from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._merge_sort(0, len(nums)-1, nums)
        return nums

    def _merge_sort(self, low: int, high: int, nums: List[int]) -> None:
        if low >= high:
            return

        mid = (low+high)//2
        self._merge_sort(low, mid, nums)
        self._merge_sort(mid+1, high, nums)

        l, r = low, mid+1
        tmp = []
        while l <= mid and r <= high:
            if nums[l] > nums[r]:
                tmp.append(nums[r])
                r += 1
            else:
                tmp.append(nums[l])
                l += 1
        while l <= mid:
            tmp.append(nums[l])
            l += 1
        while r <= high:
            tmp.append(nums[r])
            r += 1
        nums[low:high+1] = tmp
        return nums