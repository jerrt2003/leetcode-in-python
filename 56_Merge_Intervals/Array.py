# -*- coding: utf-8 -*-
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        Solution: Array
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Inspired By: MYSELF!!
        TP:
        - Sort the intervals use start as key
        - Create a empty list and push the first interval into list if list is empty
        - Go through the intervals and compare:
            - if current interval_start > pervious_interval_end(res[-1].end):
                - means there are no overlap, so just append this interval into res
            - if current interval_end > previous_interval_end(res[-1].end):
                - means there are overlap, so we need to replace previous_interval_end to current interval_end
        - return res
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=self.getStart)
        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                orig_end = res[-1].end
                if interval.start > orig_end:
                    res.append(interval)
                elif interval.end > orig_end:
                    res[-1].end = interval.end
        return res

    def getStart(self, interval):
        return interval.start