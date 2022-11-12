# -*- coding: utf-8 -*-
class Solution(object):
    def rob(self, nums):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(1)
        Perf: Runtime: 28 ms, faster than 21.96% / Memory Usage: 10.9 MB, less than 10.35%
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1:
            return nums[0]
        m = len(nums)
        # no rob last house
        res_1, prev, curr = 0, 0, 0
        for i in range(m-1):
            res_1 = max(prev+nums[i], curr)
            curr, prev = res_1, curr
        # rob last house
        res_2, prev, curr = 0, 0, 0
        for i in range(1, m):
            res_2 = max(prev+nums[i], curr)
            curr, prev = res_2, curr
        return max(res_1, res_2)

print Solution().rob([1])