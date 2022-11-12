# -*- coding: utf-8 -*-
class Solution(object):
    def wiggleSort(self, nums):
        """
        Facebook
        Solution: O(n) 1 pass Solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!! (92ms, beat 29.11%)
        TP:
        - Go through the nums list and swap number if not in right order
        - (Question: will it exist a condition where this moving break the previous order..?)
        - (Ans: No)
        - Consider this:
            7, 5, 8, 9
            1st move: 5, 7, 8, 9
            2nd move: 5, 8, 7, 9
            So it won't exist situation that 2 consecutive move break the order
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        for i in range(m - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

