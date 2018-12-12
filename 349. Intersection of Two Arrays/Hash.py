# -*- coding: utf-8 -*-
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash = dict()
        for num in nums1:
            if num not in hash:
                hash[num] = 1
        for num in nums2:
            if num in hash:
                hash[num] = 2
        ans = []
        for k, v in hash.iteritems():
            if v == 2:
                ans.append(k)
        return ans