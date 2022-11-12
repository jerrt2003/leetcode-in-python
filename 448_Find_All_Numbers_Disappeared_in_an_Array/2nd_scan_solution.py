# -*- coding: utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        Solution: O(n)
        Time Complexity: O(n) (372 ms, beat 8.2%)
        Space Complexity: O(1)
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        while i < len(nums) + 1:
            x = nums[i - 1]
            if x != i and 1 <= x <= len(nums) and nums[x-1] != x:
                nums[i - 1], nums[x-1] = nums[x-1], x
            else:
                i += 1
        res = []
        for idx, num in enumerate(nums, 1):
            if idx != num:
                res.append(idx)
        return res

nums = [4,3,2,7,8,2,3,1]
print Solution().findDisappearedNumbers(nums)

