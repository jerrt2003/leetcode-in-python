# -*- coding: utf-8 -*-
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        Solution: sorting + go through the list
        Time Complexity: O(nlog(n))
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        TP:
        - this solution is actually not meet requirement since its time complexity is O(nlog(n))
        - basic idea is to first sort the number and based on the condition to find the missing number
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        prev = 0
        for num in nums:
            if num <= 0: continue
            if num - prev > 1:
                return prev+1
            else:
                prev = num
        return prev+1 # if no missing number is found, which mean the missing number will be at the end of list

nums = [7,8,9,11,12]
sol = Solution()
print sol.firstMissingPositive(nums)