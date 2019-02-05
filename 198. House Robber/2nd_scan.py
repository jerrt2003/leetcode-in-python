# -*- coding: utf-8 -*-
class Solution(object):
    def rob(self, nums):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySelf!!
        Perf: 20ms(100%), 7MB(82.34%)
        :type nums: List[int]
        :rtype: int
        """
        rob_prev = 0
        norob_prev = 0
        res = 0
        for num in nums:
            res = max(rob_prev, norob_prev + num)
            rob_prev, norob_prev = res + num, rob_prev
        return res
