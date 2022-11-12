# -*- coding: utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        Solution: Hashtable
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/single-number/solution/
        Thinking process:
        - Create a dict
        - Iterate through nums and count its appearance
        - If num exist in the dict, pop it!! else leave alone
        - At the end only single num will remain in the dict, return it
        :type nums: List[int]
        :rtype: int
        """
        hashtable = {}
        for num in nums:
            try:
                hashtable.pop(num)
            except:
                hashtable[num] = 1
        return hashtable.popitem()[0]


