# -*- coding: utf-8 -*-
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def _permute(path, remain):
            if len(remain) == 1:
                res.append(path + remain)
                return
            else:
                for i in range(len(remain)):
                    _permute(path + remain[:1], remain[1:])
                    remain = remain[1:] + remain[:1]

        _permute([], nums)

        return res

print Solution().permute([1,2,3,4])