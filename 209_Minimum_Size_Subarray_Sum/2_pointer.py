# -*- coding: utf-8 -*-
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        Solution: 2 pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!!
        TP:
        - use 2 pointer to move along the nums
        - Time complexity will be 2*n (since travel nums twice)
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        min_l = float('inf')
        l = r = 0
        total = nums[l]
        while True:
            if l == r:
                if nums[l] >= s:
                    return 1
                else:
                    r += 1
                    if r >= len(nums): break
                    total += nums[r]
            else:
                if total >= s:
                    min_l = min(min_l, r-l+1)
                    total -= nums[l]
                    l += 1
                else:
                    r += 1
                    if r >= len(nums): break
                    total += nums[r]
        return 0 if min_l == float('inf') else min_l



#nums = [2,3,1,2,4,3]
nums = [1,2,3,4,5]
#nums = [10, 2, 3]
s = 11

print Solution().minSubArrayLen(s, nums)