# -*- coding: utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        i_min = 0
        i_max = m
        while i_min <= i_max:
            i = (i_min + i_max) / 2
            j = (m + n + 1) / 2 - i
            if (i == 0 or j == n or nums1[i - 1] <= nums2[j]) and (j == 0 or i == m or nums2[j - 1] <= nums1[i]):
                if i == 0:
                    left_max = nums2[j-1]
                elif j == 0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1], nums2[j-1])
                if (m+n) % 2 != 0:
                    return left_max
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])
                return (left_max + right_min) / 2.0
            elif i > 0 and nums1[i - 1] > nums2[j]:
                i_max = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                i_min = i + 1

nums1 = [1,3]
nums2 = [2]

print Solution().findMedianSortedArrays(nums1, nums2)