# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for k in nums1.keys():
            if k in nums2:
                if nums1[k] <= nums2[k]:
                    res.extend([k] * nums1[k])
                else:
                    res.extend([k] * nums2[k])
        return res

nums1 = [1,2,2,1]
nums2 = [2,2]
assert Solution().intersect(nums1, nums2) == [2,2]