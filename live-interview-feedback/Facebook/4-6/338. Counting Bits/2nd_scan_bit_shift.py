# -*- coding: utf-8 -*-
class Solution(object):
    def countBits(self, num):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        Perf: 116 ms, faster than 69.46% / 12.6 MB, less than 48.00%
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]
        DP = [0 for _ in range(num+1)]
        DP[0] = 0
        DP[1] = 1
        power = 0
        for i in range(2,num+1):
            if i == 2 << power:
                DP[i] = 1
                power += 1
            else:
                DP[i] = 1 + DP[i-int(2 << (power-1))]
        return DP
