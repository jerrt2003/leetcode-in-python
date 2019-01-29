# -*- coding: utf-8 -*-
class Solution(object):
    def subsets(self, nums):
        """
        Solution: Iterative
        Time Complexity: O(2^n)
        Space Complexity: O(2^n)
        Inspired By: https://leetcode.com/problems/subsets/discuss/27278/C++-RecursiveIterativeBit-Manipulation
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [_res + [num] for _res in res]
        return res