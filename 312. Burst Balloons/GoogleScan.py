# -*- coding: utf-8 -*-
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        # DP[i][j] := max coins collects between i and j
        DP = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        m = len(nums)
        for gap in range(2, m):
            for i in range(m-gap):
                j = i+gap
                for k in range(i+1, j):
                    DP[i][j] = max(DP[i][j], DP[i][k]+nums[i]*nums[k]*nums[j]+DP[k][j])
        return DP[0][m-1]


nums = [3, 1, 5, 8]
print Solution().maxCoins(nums)
