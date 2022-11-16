from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot_idx: int = 0
        # find pivot idx
        l_idx, r_idx = 0, len(nums)-1
        ## restore bs idenity if needed
        while l_idx < r_idx and nums[l_idx] == nums[r_idx]:
            r_idx -= 1
        l, r = l_idx, r_idx+1    
        while l < r:
            m = (l+r-1)//2
            if nums[m] <= nums[0]:
                r = m
            else:
                l = m+1
        if l == 0:
            pivot_idx = 1
        else:
            pivot_idx = l
        
        # check left and right for target
        return self._find_target(0, pivot_idx, target, nums) or self._find_target(pivot_idx, r_idx+1, target, nums)
        

    def _find_target(self, lower_bound: int, upper_bound: int, target: int, nums: List[int]) -> bool:
        l, r = lower_bound, upper_bound
        while l < r:
            m = (l+r-1)//2
            if nums[m] > target:
                r = m
            else:
                l = m+1
        return nums[l-1] == target
