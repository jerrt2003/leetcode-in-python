from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        j = 0
        cur_sum = 0
        ans = float("inf")
        for i in range(len(nums)):
            cur_sum += nums[i]
            while j <= i and cur_sum >= k:
                ans = min(ans, i - j + 1)
                cur_sum -= nums[j]
                j += 1
        return ans if ans != float("inf") else -1
