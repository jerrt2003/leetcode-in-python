# -*- coding: utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        Sol: Divide and Conquer
        Time: n(log(n))
        Space: log(n)
        Perf: 280ms, 20.50%
        :type nums: List[int]
        :rtype: int
        """
        def findMajority(l, r, nums):
            if l == r:
                return nums[l]
            mid = (l+r)/2
            res_l = findMajority(l, mid, nums)
            res_r = findMajority(mid+1, r, nums)
            if res_l == res_r:
                return res_l
            else:
                count_l = count(l, r, res_l, nums)
                count_r = count(l, r, res_r, nums)
                return res_l if count_l > count_r else res_r

        def count(l, r, target, nums):
            count = 0
            for i in range(l, r+1):
                if nums[i] == target:
                    count += 1
            return count

        return findMajority(0, len(nums)-1, nums)