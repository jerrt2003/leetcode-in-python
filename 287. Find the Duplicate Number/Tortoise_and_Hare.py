# -*- coding: utf-8 -*-
class Solution(object):
    def findDuplicate(self, nums):
        """
        Solution: Tortoise and Hare
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By:
        - https://leetcode.com/problems/find-the-duplicate-number/solution/
        - https://leetcode.com/problems/find-the-duplicate-number/discuss/72845/Java-O(n)-time-and-O(1)-space-solution.-Similar-to-find-loop-in-linkedlist.
        :type nums: List[int]
        :rtype: int
        """
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        ptr_1 = nums[0]
        ptr_2 = tortoise
        while ptr_1 != ptr_2:
            ptr_1 = nums[ptr_1]
            ptr_2 = nums[ptr_2]
        return ptr_2