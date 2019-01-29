# -*- coding: utf-8 -*-
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(l, r):
            if l == r:
                return l
            else:
                m = (l+r)/2
                left_idx = helper(l, m)
                right_idx = helper(m+1, r)
                if nums[left_idx] > nums[right_idx]:
                    return left_idx
                else:
                    return right_idx
        l = 0
        r = len(nums)-1
        return helper(l, r)

nums = [1,2,1,3,5,6,4]
print Solution().findPeakElement(nums)