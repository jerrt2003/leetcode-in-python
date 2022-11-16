# -*- coding: utf-8 -*-
class Solution(object):
    def findPeakElement(self, nums):
        """
        Facebook
        Binary Search
        Time Complexity: O(log(n))
        Space Complexity: O(log(n))
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return None
        def findPeak(l, r):
            if l == r:
                return l
            mid = (l+r)/2
            l_peak = findPeak(l, mid)
            r_peak = findPeak(mid+1, r)
            if nums[l_peak] > nums[r_peak]:
                return l_peak
            else:
                return r_peak

        l = 0
        r = len(nums)-1
        return findPeak(l, r)

nums = [-1, -10, 5, 3, 100, 21, 30, 100]