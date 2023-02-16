import collections, random

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.freq = collections.Counter(nums)
        candidates = [k for k in self.freq.keys()]
        self.quick_select(candidates, 0, len(candidates)-1, len(candidates)-k)
        return candidates[len(candidates)-k:]

    def quick_select(self, nums: List[int], l: int, r: int, k: int) -> None:
        if l >= r:
            return
        mid = self.partition(nums, l, r)
        if mid == k:
            return
        elif mid > k:
            self.quick_select(nums, l, mid-1, k)
        else:
            self.quick_select(nums, mid+1, r, k)

    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivot_idx = random.randint(l, r)
        pivot = nums[pivot_idx]
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
        i, j = l, r
        while i < j:
            while i < j and self.freq[nums[j]] >= self.freq[pivot]:
                j -= 1
            nums[i] = nums[j]
            while i < j and self.freq[nums[i]] <= self.freq[pivot]:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        # 需要回傳i而不是pivot_idx因為nums[i]才是最後的大於小於nums[pivot_idx]
        # 的分界點
        return i
