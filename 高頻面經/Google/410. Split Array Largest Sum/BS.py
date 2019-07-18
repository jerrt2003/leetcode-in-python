# -*- coding: utf-8 -*-
class Solution(object):
    def splitArray(self, nums, m):
        """
        - 原题问的是把最大值尽可能变小，总共要K份可以把他想成一个Bar Graph，
          每一个subarray sum是一个Bar，总共要至少K个Bar，而且最高的那个Bar不得超过二分法猜的 Target.
          二分法的过程中我们要尽可能的把那个Target压小,直到Target再小一格的话就达不到 K 个Bar了.
          使用左闭右开的二分法模板，最后left的数值是“符合条件的最小数字”,在这一题的条件就是至少要K个Bar，而每个Bar都不能超过猜测的Target,
          所以left 会得到最小化的最大值．
        - Perf: Runtime: 24 ms, faster than 72.53% / Memory Usage: 11.8 MB, less than 14.89%
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValid(target):
            total = 0
            count = 1
            for num in nums:
                total += num
                if total > target:
                    count += 1
                    total = num
                    if count > m:
                        return False
            return True

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l+r) / 2
            if isValid(mid):
                r = mid
            else:
                l = mid+1
        return l

#nums = [7,2,5,10,8,7,2,5,10,8]
#m = 5

nums = [1,2147483647]
m = 2

#nums = [7,2,5,10,8]
#m = 2

print Solution().splitArray(nums, m)

