# -*- coding: utf-8 -*-
class Solution(object):
    def findNum(self, nums):
        num1 = nums[len(nums)/4]
        num2 = nums[len(nums)/2]
        num3 = nums[len(nums)/4 * 3]

        def findLowerBound(target):
            l, r = 0, len(nums)
            while l < r:
                m = (l+r-1)/2
                if nums[m] >= target:
                    r = m
                else:
                    l = m+1
            return l

        def findUpperBound(target):
            l, r = 0, len(nums)
            while l < r:
                m = (l+r-1)/2
                if nums[m] > target:
                    r = m
                else:
                    l = m+1
            return l-1

        def check(lower, upper):
            total = upper - lower + 1
            if total > len(nums)/4.0:
                return True

        for num in (num1, num2, num3):
            lower = findLowerBound(num)
            upper = findUpperBound(num)
            if check(lower, upper):
                return num

assert Solution().findNum([1,2,2,6,6,6,6,7,10]) == 6