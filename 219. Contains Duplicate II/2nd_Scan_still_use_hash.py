# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup = hash2.defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in dup and i - dup[nums[i]][-1] <= k:
                return True
            else:
                dup[nums[i]].append(i)
        return False