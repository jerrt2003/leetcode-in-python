# -*- coding: utf-8 -*-
class Solution(object):
    def checkPossibility(self, nums):
        """
        Time: O(n)
        Space: (1)
        Perf: Runtime: 168 ms, faster than 69.73% / Memory Usage: 12.6 MB, less than 68.90%
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                p = i

        return (p == None or p == 0 or p == len(nums) - 2 or nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2])

assert Solution().checkPossibility([4,2,1])