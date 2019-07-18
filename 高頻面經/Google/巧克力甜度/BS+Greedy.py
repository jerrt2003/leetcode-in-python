# -*- coding: utf-8 -*-
class Solution(object):
    def chocolate(self, nums, k):

        def isValid(mid):
            total = 0
            count = 0
            for num in nums:
                total += num
                if total >= mid:
                    count += 1
                    total = 0
            return count < k

        l, r = min(nums), sum(nums)+1
        while l < r:
            mid = (l+r-1)/2
            if isValid(mid):
                r = mid
            else:
                l = mid+1
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