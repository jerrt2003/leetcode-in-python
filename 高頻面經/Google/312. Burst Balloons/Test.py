# -*- coding: utf-8 -*-
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        nums = [1] + nums + [1]
        DP = [[0 for _ in range(m+2)] for _ in range(m+2)]
        for l in range(1, m+1):
            for i in range(1,m-l+2):
                j = i+l-1
                for k in range(i, j+1):
                    DP[i][j] = max(DP[i][j], DP[i][k-1]+DP[k+1][j]+nums[i-1]*nums[k]*nums[j+1])
        return DP[1][m]

assert Solution().maxCoins([3,1,5,8]) == 167