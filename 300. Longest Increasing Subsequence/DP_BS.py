# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Solution: DP + BS
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Inspired By:
        - https://segmentfault.com/a/1190000003819886#articleHeader1
        - https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        - https://yanjia.me/zh/2018/11/05/70/
        TP:
        - ...
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        def findIndex(DP, l, r, target):
            while l < r:
                m = (l+r)/2
                if DP[m] < target:
                    l = m+1
                else:
                    r = m
            return l

        nums_len = len(nums)
        DP = [0 for _ in range(nums_len+1)]
        DP[0] = nums[0]
        max_len = 1
        for i in range(1, nums_len):
            if nums[i] < DP[0]:
                DP[0] = nums[i]
            elif nums[i] > DP[max_len-1]:
                DP[max_len] = nums[i]
                max_len += 1
            else:
                DP[findIndex(DP, 0, max_len-1, nums[i])] = nums[i]
        return max_len

#nums = [10,9,2,5,3,7,101,18]
#nums = []
nums = [1,3,6,5,7]
print Solution().lengthOfLIS(nums)