# -*- coding: utf-8 -*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start = self.bs(nums, target)
        print start
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.bs(nums, target + 1)
        return [start, end - 1]

    def bs(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r - 1) / 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l