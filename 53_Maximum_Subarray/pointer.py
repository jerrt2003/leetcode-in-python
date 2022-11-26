from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans: int = 0
        tmp_sum :int = 0
        l = 0
        for r in range(0, len(nums)):
            prev_sum = tmp_sum
            tmp_sum += nums[r]
            if tmp_sum < prev_sum:
                while l < r:
                    tmp_sum -= nums[l]
                    if tmp_sum >= prev_sum:
                        break
                    l += 1
            ans = max(ans, tmp_sum)
        return ans
