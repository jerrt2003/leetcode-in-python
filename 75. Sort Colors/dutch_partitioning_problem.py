# -*- coding: utf-8 -*-
class Solution(object):
    def sortColors(self, nums):
        """
        Solution: Dutch Partitioning
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By:
        - https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
        - https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
