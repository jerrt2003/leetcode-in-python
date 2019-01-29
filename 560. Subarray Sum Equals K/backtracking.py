# -*- coding: utf-8 -*-
class Solution(object):
    def subarraySum(self, nums, k):
        """
        Solution: Backtracking
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Inspired By: MySELF!! (9460ms, beat 18.56%)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.res = 0
        def helper(curr_sum, nums, k):
            if curr_sum == k:
                self.res += 1
            for num in nums:
                curr_sum += num
                if curr_sum == k:
                    self.res += 1
        for i in range(len(nums)):
            helper(nums[i], nums[i+1:], k)
        return self.res

nums = [1,1,1]
k = 2
print Solution().subarraySum(nums, k)