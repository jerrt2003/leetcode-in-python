# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
class Solution(object):
    def countBits(self, num):
        """
        Perf: Runtime: 64 ms, faster than 95.96% / Memory Usage: 15.8 MB, less than 37.10%
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
                rem = i - (1<<k-1)
                res.append(1+res[rem])
        return res


