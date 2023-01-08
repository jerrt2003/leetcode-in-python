import random

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_select(len(nums)-k, 0, len(nums)-1, nums)
        return nums[len(nums)-k]
        
    def quick_select(self, k: int, l: int, r: int, nums: List[int]) -> None:
        """a split method
        寻找到第k个数停止递归
        使得nums数组中index左边是前k个小的数
        index右边是后面n-k个大的数
        Args:
            k (int): 常數k 題目定義
            l (int): 左邊界
            r (int): 右邊界
            nums (List[int]): 數組
        """
        if l >= r:
            return
        idx = self.partition(l, r, nums)
        if idx == k:
            return
        elif idx > k:
            self.quick_select(k, l, idx-1, nums)
        else:
            self.quick_select(k, idx+1, r, nums)

    def partition(self, l: int, r: int, nums: List[int]) -> int:
        pivot_idx = random.randint(l, r)
        pivot = nums[pivot_idx]
        # swap first value with pviot
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
        lb, rb = l, r
        while lb < rb:
            while lb < rb and nums[rb] >= pivot:
                rb -= 1
            nums[lb] = nums[rb]
            while lb < rb and nums[lb] <= pivot:
                lb += 1
            nums[rb] = nums[lb]
        nums[lb] = pivot
        return lb

    