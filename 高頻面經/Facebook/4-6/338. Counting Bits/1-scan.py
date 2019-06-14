# -*- coding: utf-8 -*-
class Solution(object):
    def countBits(self, num):
        """
        Perf: Runtime: 76 ms, faster than 67.50% / Memory Usage: 15.8 MB, less than 34.27%
        :type num: int
        :rtype: List[int]
        """
        k = 0
        res = [0]
        for i in range(1, num+1):
            if i == (1<<k):
                res.append(1)
                k += 1
            else:
                rem = i - (1<<k)
                res.append(1+res[rem])
        return res

#assert Solution().countBits(2) == [0,1,1]
#assert Solution().countBits(5) == [0,1,1,2,1,2]
assert Solution().countBits(14)