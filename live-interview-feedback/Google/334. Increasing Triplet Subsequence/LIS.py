# -*- coding: utf-8 -*-
class Solution(object):
    def increasingTriplet(self, nums):
        """
        Use LIS concept to do it
        T: O(n)
        S: O(1)
        Perf: Runtime: 44 ms, faster than 62.91% / Memory Usage: 12.3 MB, less than 29.05%
        :type nums: List[int]
        :rtype: bool
        """
        A = float('inf')
        B = float('inf')
        for num in nums:
            if num < A:
                A = num
            elif A < num < B:
                B = num
            elif num > B:
                return True
        return False
