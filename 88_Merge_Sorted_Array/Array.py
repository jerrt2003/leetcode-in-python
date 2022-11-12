# -*- coding: utf-8 -*-
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Solution: Array
        Time Complexity: O(m+n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/merge-sorted-array/discuss/29522/This-is-my-AC-code-may-help-you
        TP:
        - Tricky one, if we start algorithm from beginning, we'll hit "0" which can't resolve
        - Need to sort backwards
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while i >=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        return nums1

    sorted()

a = [1,2,3,0,0,0]
m = 3
b = [2,5,6]
n = 3

sol = Solution()
print sol.merge(a, m, b, n)