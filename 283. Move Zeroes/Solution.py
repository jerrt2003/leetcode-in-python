# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        Solution: BAD one
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                idx = i
                while nums[idx-1] == 0 and idx-1 >= 0:
                    nums[idx-1] = nums[idx]
                    nums[idx] = 0
                    idx -= 1
        return nums

nums = [0,0,1,0,3,12,0,4]
sol = Solution()
print sol.moveZeroes(nums)