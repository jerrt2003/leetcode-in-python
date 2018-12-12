# -*- coding: utf-8 -*-
class Solution(object):
    def arrayPairSum(self, nums):
        """
        Solution: Order the list
        Time Complexity: O(n*log(n))
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        TP:
        - find max maximum sum of min(a1, b1)
        - Ordered the list and put smallest on one side as much as possible
        - Return sum
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res
