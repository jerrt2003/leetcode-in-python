# -*- coding: utf-8 -*-
import math
class Solution(object):
    def countBits(self, num):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        Perf: 148 ms, faster than 39.40% / 12.6 MB, less than 22.50%
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]
        DP = [0 for _ in range(num+1)]
        DP[0] = 0
        DP[1] = 1
        power = 1
        for i in range(2,num+1):
            if i == math.pow(2, power):
                DP[i] = 1
                power += 1
            else:
                DP[i] = 1 + DP[i-int(math.pow(2,power-1))]
        return DP
