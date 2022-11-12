# -*- coding: utf-8 -*-
class Solution(object):
    def splitArray(self, nums, m):
        """
        Solution: DP
        Time Complexity: O(n^2*m)
        Space Complexity: O(n*m)
        Perf: Runtime: 4708 ms, faster than 10.73% / Memory Usage: 12.5 MB, less than 14.89%
        Inspired By: https://leetcode.com/problems/split-array-largest-sum/solution/ (DP solution)
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        DP = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
        DP[0][0] = 0
        num_sum = [0]
        for i in range(1, n+1):
            num_sum.append(num_sum[-1]+nums[i-1])
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    DP[i][j] = min(DP[i][j], max(DP[k][j-1], num_sum[i]-num_sum[k]))
        return DP[-1][-1]