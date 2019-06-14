# -*- coding: utf-8 -*-
# http://tinyurl.com/y33mvyb2
# 2019(1-3)
# Leetcode #253
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        Sol: heap
        Time: O(nlog(n)) # heap作push/pop都是log(n), 總共有n組intervals, so total O(nlog(n))
        Space: O(n)
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda k: k[0]) # need to sort meeting room schedule based on start time
        pq = []
        for s, e in intervals:
            if not pq:
                pq.append(e)
            else:
                if s >= pq[0]: # start == end, just need 1 meeting room
                    heapq.heappushpop(pq, e)
                else:
                    heapq.heappush(pq, e)
        return len(pq)

assert Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]) == 2
assert Solution().minMeetingRooms([[5, 10],[0, 30],[15, 20]]) == 2
assert Solution().minMeetingRooms([[5, 10],[15, 20]]) == 1
assert Solution().minMeetingRooms([[7,10],[2,4]]) == 1

