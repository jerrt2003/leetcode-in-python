# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        Solution: Fill empty with 0
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/move-zeroes/discuss/72011/Simple-O(N)-Java-Solution-Using-Insert-Index
        TP:
        - move all non-0 digits as far left as possible
        - record the last non-0 idx
        - fill 0 for position between last non-0 idx and len(nums)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastNoneZeroIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNoneZeroIdx] = nums[i]
                lastNoneZeroIdx += 1
        for i in range(lastNoneZeroIdx, len(nums)):
            nums[i] = 0
        print nums

nums = [1,0,3,0,0,7]
sol = Solution()
sol.moveZeroes(nums)
