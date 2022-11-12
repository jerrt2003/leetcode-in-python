# -*- coding: utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        Solution: O(n) solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        TP:
        - put every number to its right position
        - once done check any number which is not at its "designated" position
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        i = 1
        while i < len(nums)+1:
            x = nums[i-1]
            if x != i and nums[x-1] != x:
                nums[i-1], nums[x-1] = nums[x-1], x
            else:
                i += 1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                res.append(i+1)
        return res

nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print sol.findDisappearedNumbers(nums)