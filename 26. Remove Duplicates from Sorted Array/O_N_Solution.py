# -*- coding: utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!! (68ms, beat 53.11%)
        TP:
        - mark the last indistinct number idx (in this code: length)
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        last = None
        for num in nums:
            if num != last:
                nums[length] = num
                last = num
                length += 1
        return length
