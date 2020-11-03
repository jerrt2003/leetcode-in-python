# -*- coding: utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        DP = [0] * len(nums)
        DP[0] = currMax = nums[0]
        for i in range(1, len(nums)):
            DP[i] = max(DP[i-1], 0)+nums[i]
            currMax = max(DP[i], currMax)
        return currMax
        '''
        '''
        curr_max = finalMax = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(curr_max, 0)+nums[i]
            finalMax = max(curr_max, finalMax)
        return finalMax
        '''

        DP = [0] * len(nums)
        DP[0] = nums[0]
        for i in range(1, len(nums)):
            DP[i] = max(DP[i-1]+nums[i], nums[i])
        return max(DP)

assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6