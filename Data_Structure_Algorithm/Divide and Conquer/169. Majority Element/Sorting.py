# -*- coding: utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        Solution: Sorting
        Time Complexity: O(nlog(n))
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/majority-element/solution/
        TP:
        - The most straight forward thought is to use dict, which will result O(n) time and O(n) space
        - But we can sort the element and "majority" number must occur @ n/2
            - The problem specified that "majority" number must be there
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums)/2]
