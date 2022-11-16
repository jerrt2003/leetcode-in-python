from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        # find the pivot point
        l, r = 0, len(nums)
        while l < r:
            m = (l+r-1)//2
            if nums[m] < nums[0]:
                r = m
            else:
                l = m+1
        if l == len(nums):
            pivot_idx = 0
        else:
            pivot_idx = l                
        # decide where the target could be landed
        if nums[pivot_idx] <= target <= nums[-1]:
            l_final, r_final = pivot_idx, len(nums)
        else:
            l_final, r_final = 0, pivot_idx
        # check if target is there
        while l_final < r_final:
            m = (l_final+r_final-1)//2
            if nums[m] > target:
                r_final = m
            else:
                l_final = m+1
        return l_final-1 if nums[l_final-1] == target else -1
