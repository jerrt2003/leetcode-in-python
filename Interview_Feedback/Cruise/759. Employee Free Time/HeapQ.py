# -*- coding: utf-8 -*-
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        T: O(nlog(n))
        S: O(n)
        Perf: Runtime: 260 ms, faster than 31.09% / Memory Usage: 17.2 MB, less than 12.50%
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        res = []
        pq = []
        for sch in schedule:
            for interval in sch:
                heapq.heappush(pq, (interval.start, interval.end))

        currStart, currEnd = heapq.heappop(pq)

        while pq:
            nextStart, nextEnd = heapq.heappop(pq)
            if nextEnd <= currEnd: continue
            elif nextStart <= currEnd:
                currStart = currEnd
                currEnd = nextEnd
            else:
                res.append(Interval(currEnd, nextStart))
                currStart = nextStart
                currEnd = nextEnd

        return res