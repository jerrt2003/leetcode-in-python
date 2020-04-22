# -*- coding: utf-8 -*-
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ##############
        # Using Sum  #
        ##############
        '''
        numSum = sum(nums)
        if numSum % 2 != 0:
            return False

        targetSum = numSum / 2

        DP = [[0 for _ in range(targetSum+1)] for _ in range(len(nums)+1)]

        for i in range(1, len(nums)+1):
            for j in range(1, targetSum+1):
                if nums[i-1] <= j:
                    cur = nums[i-1] + DP[i-1][j-nums[i-1]]
                    DP[i][j] = max(DP[i-1][j], cur)
                else:
                    DP[i][j] = DP[i-1][j]
                if DP[i][j] == targetSum:
                    return True

        return DP[-1][-1] == targetSum
        '''
        ##################
        # Using Boolean  #
        ##################
        '''
        numsSum = sum(nums)
        if numsSum % 2 != 0:
            return False

        n = numsSum / 2
        m = len(nums)

        DP = [[False for _ in range(n+1)] for _ in range(m+1)]

        DP[0][0] = True

        for i in range(1, m+1):
            DP[i][0] = True

        for j in range(1, n+1):
            DP[0][j] = False

        for i in range(1, m+1):
            for j in range(1, n+1):
                DP[i][j] = DP[i-1][j]
                if j >= nums[i-1]:
                    DP[i][j] = DP[i-1][j] or DP[i-1][j - nums[i-1]]

        return DP[-1][-1]
        '''
        ##################
        # 空間優化        #
        ##################
        numSum = sum(nums)
        if numSum % 2 != 0:
            return False

        m = len(nums)
        n = numSum / 2

        DP = [False] * (n+1)
        DP[0] = True

        for i in range(1, m+1):
            for j in range(n, 0, -1):
                if nums[i-1] <= j:
                    DP[j] = DP[j] or DP[j-nums[i-1]]

        return DP[-1]
