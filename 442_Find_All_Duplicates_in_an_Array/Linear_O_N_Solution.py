# -*- coding: utf-8 -*-
class Solution(object):
    def findDuplicates(self, nums):
        """
        Solution: O(n) Linear Solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - put number into correct position as much as possible
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        while i < len(nums)+1:
            x = nums[i-1]
            if x != i and nums[x-1] != x:
                nums[i-1], nums[x-1] = nums[x-1], x
            else:
                i += 1
        res = []
        for p, q in enumerate(nums, 1):
            if p != q:
                res.append(q)
        return res