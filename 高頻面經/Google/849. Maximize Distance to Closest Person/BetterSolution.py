# -*- coding: utf-8 -*-
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        last, maxDist = -1, -float('inf')
        for i in range(len(seats)):
            if seats[i]:
                maxDist = max(maxDist, i if last < 0 else (i-last)/2)
                last = i
        return max(maxDist, len(seats)-1-last)

assert Solution().maxDistToClosest([1,0,0,0,1,0,1]) == 2