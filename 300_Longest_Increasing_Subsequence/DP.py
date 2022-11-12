# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Solution: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/longest-increasing-subsequence/solution/
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        max_len = 1
        len_nums = len(nums)
        DP = [0 for _ in range(len_nums)]
        for i in range(len_nums):
            _max = 0
            for j in range(i+1):
                if nums[i] > nums[j]:
                    _max = max(_max, DP[j])
            DP[i] = _max+1
            max_len = max(max_len, DP[i])
        return max_len

nums = [10,9,2,5,3,7,101,18]
print Solution().lengthOfLIS(nums)

