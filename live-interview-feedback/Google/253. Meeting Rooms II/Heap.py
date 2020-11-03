# -*- coding: utf-8 -*-
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        Solution: Heapq + Sorting
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 80 ms, faster than 22.20% / Memory Usage: 17.9 MB, less than 5.35%
        Inspired By: https://leetcode.com/problems/meeting-rooms-ii/solution/
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        schedule = []
        for interval in intervals:
            if not schedule:
                schedule.append(interval.end)
            else:
                if interval.start >= schedule[0]:
                    heapq.heappushpop(schedule, interval.end)
                else:
                    heapq.heappush(schedule, interval.end)
        return len(schedule)

