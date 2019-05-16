# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonZeroIdx = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != 0:
                nums[nonZeroIdx] = nums[i]
                nonZeroIdx -= 1

        for i in range(nonZeroIdx+1):
            nums[i] = 0

        return nums

input = [1,0,3,0,0,9,0,0]
print Solution().moveZeroes(input)