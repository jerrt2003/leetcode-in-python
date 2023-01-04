from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[int] = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)

