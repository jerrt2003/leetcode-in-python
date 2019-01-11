# -*- coding: utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        """
        Solution: O(n)
        Time Complexity: O(n) (44ms, beat 9%)
        Space Complexity: O(1)
        TP:
        - record the last idx that nums[idx] == val
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        last = None
        for i in range(len(nums)):
            if last is None and nums[i] == val:
                last = i
            elif nums[i] != val and last != None:
                nums[last] = nums[i]
                last += 1
        return last


nums = [3,3]
val = 3
print Solution().removeElement(nums, val)