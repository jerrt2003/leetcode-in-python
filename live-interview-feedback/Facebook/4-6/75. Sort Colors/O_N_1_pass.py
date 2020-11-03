# -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        Solution: O_N_1_pass
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation/200308
        TP:
        - Imagine p1 and p2 are separators for the three sections, and p is my scan pointer
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ptr1, ptr2, p = 0, len(nums)-1, 0
        while p <= ptr2:
            if nums[p] == 0:
                nums[ptr1], nums[p] = nums[p], nums[ptr1]
                ptr1 += 1
                p += 1
            elif nums[p] == 1:
                p += 1
            else: # nums[p] == 2 situation
                nums[ptr2], nums[p] = nums[p], nums[ptr2]
                ptr2 -= 1
        print nums

#nums = [2,0,2,1,1,0]
#nums = [2,2,2,2,2,2,1,1,1,1,1,1,0,0,0,0,0]
#nums = []
#nums = [0,0,0,0,1,1,1,1,2,2,2,2]
#nums = [1,0,1]
nums = [1]
Solution().sortColors(nums)