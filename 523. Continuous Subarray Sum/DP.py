# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        rem = collections.defaultdict(int)
        rem[0] = -1
        sum = 0
        for i, v in enumerate(nums):
            if k != 0:
                sum += v
                _rem = sum
            else:
                _rem = sum % k
            if _rem in rem and i - rem[_rem] >= 2:
                return True
            else:
                rem[_rem] = i
        return False

'''
arr = [23, 2, 4, 6, 7]
k = 6

assert Solution().checkSubarraySum(arr, k) == True

arr = [23, 2, 10, 4, 7]
k = 6

assert Solution().checkSubarraySum(arr, k) == True

arr = [2, 0]
k = 2
assert Solution().checkSubarraySum(arr, k) == True
'''
arr = [0, 0]
k = 0
assert Solution().checkSubarraySum(arr, k) == True

'''
arr = [0,1,0]
k = 0
assert Solution().checkSubarraySum(arr, k) == False
'''