import random
from typing import List


# quick select
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        self.nums = nums
        l, r = 0, len(nums) - 1

        self.quick_select(l, r, len(nums) - k)

        return self.nums[len(nums) - k]

    def quick_select(self, l, r, k) -> None:
        if l >= r:
            return
        mid = self.partition(l, r)
        if mid == k:
            return
        elif mid > k:
            self.quick_select(l, mid - 1, k)
        else:
            self.quick_select(mid + 1, r, k)

    def partition(self, l, r) -> int:
        pivot_idx = random.randint(l, r)
        pivot = self.nums[pivot_idx]

        self.nums[l], self.nums[pivot_idx] = self.nums[pivot_idx], self.nums[l]

        while l < r:
            while l < r and int(self.nums[r]) >= int(pivot):
                r -= 1
            self.nums[l] = self.nums[r]
            while l < r and int(self.nums[l]) <= int(pivot):
                l += 1
            self.nums[r] = self.nums[l]

        self.nums[l] = pivot
        return l
