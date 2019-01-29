# -*- coding: utf-8 -*-
class Solution(object):
    def jump(self, nums):
        """
        Solution: DP (TLE)
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        TP:
        - Using DP to log min jump to i-th position
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        DP = [float('inf') for _ in range(m)]
        DP[0] = 0
        for i in range(m):
            if i + nums[i] >= len(nums)-1:
                return DP[i] + 1
            for j in range(i+1, min(m, i + nums[i]+1)):
                DP[j] = min(DP[j], DP[i]+1)

nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4]
print Solution().jump(nums)
