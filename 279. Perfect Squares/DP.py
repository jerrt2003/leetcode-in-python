# -*- coding: utf-8 -*-
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [0, 1, 2]
        if n < 3:
            return DP[n]
        base = 2
        prev_power = 1
        for i in range(3, n+1):
            power = int(pow(base, 2))
            if i == power:
                DP.append(1)
                prev_power = power
                base += 1
            else:
                DP.append(1 + DP[i - prev_power])
        return DP[-1]


n = 12
print Solution().numSquares(n)