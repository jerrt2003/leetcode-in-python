# -*- coding: utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        max_so_far = max_end_here = nums[0]
        for i in range(1, len(nums)):
            max_end_here = max(max_end_here+nums[i], nums[i])
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-2, -1, -3]
print Solution().maxSubArray(nums)