# -*- coding: utf-8 -*-
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        Solution: use arrive time to determine if there is a hit or not
        Time: O(nlog(n))
        Space: O(n)
        Perf: Runtime: 152 ms, faster than 99.71% / Memory Usage: 14.3 MB, less than 43.81%
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        posSpeedMaps = zip(position, speed)
        posSpeedMaps.sort(key=lambda p:-p[0])
        arriveTime, res = 0, 0
        for pos, sp in posSpeedMaps:
            _arriveTime = (target-pos)/(sp*1.0)
            if _arriveTime > arriveTime:
                res += 1
                arriveTime = _arriveTime
        return res