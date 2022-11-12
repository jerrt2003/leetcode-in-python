# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m == 0: return 0
        DP = [1 for _ in range(m)]
        for i in range(1, m):
            for j in range(i):
                if nums[i] > nums[j]:
                    DP[i] = max(DP[i],DP[j] + 1)
        return max(DP)
