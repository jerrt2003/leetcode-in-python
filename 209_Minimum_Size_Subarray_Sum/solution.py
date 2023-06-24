from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # curr sum
        curr_sum = 0

        # ans
        ans = float("inf")

        # l, r
        l, r = 0, 0

        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                if (r - l + 1) < ans:
                    ans = r - l + 1
                curr_sum -= nums[l]
                l += 1
            r += 1

        return 0 if ans == float("inf") else ans
