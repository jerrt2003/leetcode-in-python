# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup = collections.defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in dup and i - dup[nums[i]][-1] <= k:
                return True
            else:
                dup[nums[i]].append(i)
        return False