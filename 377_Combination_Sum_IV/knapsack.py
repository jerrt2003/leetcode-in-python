# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = len(nums)
        if m == 0:
            return 0

        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]

        return dp[-1]

nums = [1, 2, 3]
target = 4
assert Solution().combinationSum4(nums, target) == 7