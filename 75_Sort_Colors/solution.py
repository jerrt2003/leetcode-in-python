from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1 # l is the next idx candidate for 0 while r is next idx candidate for blue
        idx = 0
        while idx <= r:
            if nums[idx] == 0:
                nums[l], nums[idx] = nums[idx], nums[l]
                l += 1
                idx += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums[r], nums[idx] = nums[idx], nums[r]
                r -= 1