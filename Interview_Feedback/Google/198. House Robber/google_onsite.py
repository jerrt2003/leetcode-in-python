# -*- coding: utf-8 -*-
class Solution(object):
    def rob(self, nums):
        """
        DP pattern:
        Input -> O(n)
        Sub-problem -> O(n)
        Depends-on -> O(1)

        Time: O(n)
        Space: O(n)->O(1)
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        prev_norob = 0
        prev_rob = 0
        curr_max = 0
        for i in range(m):
            curr_max = max(prev_norob+nums[i], prev_rob)
            prev_norob, prev_rob = prev_rob, curr_max
        return curr_max

