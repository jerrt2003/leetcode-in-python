# -*- coding: utf-8 -*-
class Solution:
    def maxProduct(self, nums):
        """
        Solution: Kadane O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - Apply same logic like Kadane Algorithm
        - Similar to Q.53
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        rmax = nums[0]
        rmin = nums[0]
        for num in nums[1:]:
            pre_rmax = rmax
            rmax = max(max(rmax*num, rmin*num), num)
            rmin = min(min(pre_rmax*num, rmin*num),num)
            res = max(res, rmax)
        return res