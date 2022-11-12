# -*- coding: utf-8 -*-
"""
From: https://www.1point3acres.com/bbs/thread-499490-1-1.html
"""
class Solution(object):
    def chocolate(self, nums, n):
        """
        同理，我们也把题目想成一个Bar Graph，每一个subarray sum 是一个Bar，总共至少K个Bar，
        而这一次我们要让所有的Bar都至少达标一个猜测的Target，这样Target就是Bar Graph的最小值．
        二分法的过程中我们要尽可能的把这个猜测的Target变大，直到再变大一格就没办法分成K份了．
        可是如果要把猜测的数值尽可能变大，就没办法直接套用左闭右开的二分法模板了．
        其他的二分法模板应该能解决，但我很任性就只想记一种模板，所以为何不把二分法确认的条件换一下？
        我们也可以去猜一个Target，要求每一个Bar 都要Target，但如果用了这个Target 就不足以分成K份了，
        找这个Target的最小值．也就是说：使用二分法会找到一个最小值的Target，虽然不能分成K份，但它已经小到再小一格就能分成K份了．
        使用左闭又开模板Left会得到这个Target，所以Left-1就刚刚好是能分成K份的最大化最小值．
        :param nums:
        :param n:
        :return:
        """
        l, r = min(nums), sum(nums)+1

        def isValid(target):
            total = 0
            count = 0
            for num in nums:
                total += num
                if total >= target:
                    count += 1
                    total = 0
            return count >= n

        while l < r:
            mid = (l+r-1)/2
            if isValid(mid):
                l = mid+1
            else:
                r = mid

        return l-1

nums = [3, 4, 5, 5, 6]
k = 4
assert Solution().chocolate(nums, k) == 5
nums = [3, 4, 5, 5, 6]
k = 3
assert Solution().chocolate(nums, k) == 6
nums = [5, 5, 6, 7, 8, 9, 9, 5]
k = 8
assert Solution().chocolate(nums, k) == 5
nums = [5, 5, 6, 7, 8, 9, 9, 5]
k = 7
assert Solution().chocolate(nums, k) == 5
nums = [5, 5, 6, 7, 8, 9, 9, 5]
k = 1
assert Solution().chocolate(nums, k) == 54
nums = [5, 3, 4, 4]
k = 2
assert Solution().chocolate(nums, k) == 8
nums = [5, 3, 4, 4]
k = 3
assert Solution().chocolate(nums, k) == 4
nums = [4, 4, 4, 4]
k = 4
assert Solution().chocolate(nums, k) == 4