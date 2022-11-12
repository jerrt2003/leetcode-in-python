# -*- coding: utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        Solution: Bit Manipulation (XOR)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/single-number/solution/
        Thinking process:
        - XOR
            - bit 1 xor bit 0 = 1
            - (bit 1 xor bit 1) or (bit 0 xor bit 0) will be 0
        - We can go through the nums and XOR all nums. What ever left if the ans
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
