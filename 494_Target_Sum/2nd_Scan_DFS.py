# -*- coding: utf-8 -*-
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.res = 0

        def dfs(curr_sum, nums):
            if curr_sum == S and not nums:
                self.res += 1
                return
            if not nums:
                return
            cand = nums.pop(0)
            for sym in (1, -1):
                dfs(cand * sym + curr_sum, nums[:])

        dfs(0, nums)
        return self.res

nums = [1,1,1,1,1]
S = 3

print Solution().findTargetSumWays(nums, S)

