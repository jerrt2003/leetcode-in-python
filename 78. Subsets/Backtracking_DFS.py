# -*- coding: utf-8 -*-
class Solution(object):
    def subsets(self, nums):
        """
        Solution: DFS + Backtracking
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! (64ms, beat 11.56%)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def DFS(nums, path):
            res.append(path)
            if not nums:
                return
            for i in range(len(nums)):
                DFS(nums[i + 1:], path + [nums[i]])

        DFS(nums, [])
        return res
