# -*- coding: utf-8 -*-
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]


assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4