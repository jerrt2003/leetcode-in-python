# -*- coding: utf-8 -*-
class Solution(object):
    def searchInsert(self, nums, target):
        """
        Solution: Binary Search
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        Inspired By: MySELF!!
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)/2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        if nums[m] > target:
            return m
        else:
            return m+1

#nums = [1,3,5,6]
nums = [1]
target = 0

print Solution().searchInsert(nums,target)
