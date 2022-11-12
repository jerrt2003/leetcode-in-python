# -*- coding: utf-8 -*-
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        last_iter = 0
        for idx, num in enumerate(sorted(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                tmp = res[len(res)-last_iter:]
                for _tmp in tmp:
                    res.append(_tmp+[num])
            else:
                last_iter = len(res)
                res += [_res + [num] for _res in res]
        return res

print Solution().subsetsWithDup([1,1])