# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        Solution: Hashset
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time
        TP:
        - Using hashset to store idx information
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = dict()
        for i in range(len(nums)):
            if nums[i] in check:
                return [check[nums[i]], i]
            else:
                check[target - nums[i]] = i

#nums = [-2, -7, -11, -15]
nums = [3,3]
target = 6

print Solution().twoSum(nums, target)