from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        DP = [0 for _ in range(len(nums))]
        DP[0] = nums[0]
        for i in range(1, len(nums)):
            DP[i] = max(DP[i-1] + nums[i], nums[i])
        return max(DP)
