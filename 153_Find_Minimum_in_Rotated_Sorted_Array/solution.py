from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r-1)//2
            if nums[m] < nums[0]:
                r = m
            else:
                l = m+1
        return nums[0] if l == len(nums) else nums[l] # l == len(nums) -> can't find m --> array is sorted already